# retrieve ELF file list
# http://www.openx.com/docs/openx_help_center/content/event_feeds_retrievinglist.html

import re
import decimal
import logging
from collections import defaultdict

import ox3apiclient
import dateutil.parser

import spendata.models

logger = logging.getLogger(__name__)

email = "montavotestacct@outlook.com"
password = "M0ntav0Test"
domain = "montavo-ui3.openxenterprise.com"
realm = "montavo_ad_server"
consumer_key = "1a81f2a240f1c3bf78af1353200c9839cb3cad91"
consumer_secret = "30650b5112c2d6050732c90e74b57e0a01c28212"

class OpenXDataRetriever(object):


    # OpenX datatypes we're interested in - e.g. account: /a/account/123 
    DATA_TYPES = ['account', 'user', 'role', 'site', 'adunit', 'adunitgroup', 'order',
        'lineitem', 'ad', 'creative', 'rule', 'report']
        
    
    _parsers = defaultdict(dict)
    
    def __init__(self):
        logger.info('OX Logging on...')
        
        self.ox = ox3apiclient.Client(
            email=email,
            password=password,
            domain=domain,
            realm=realm,
            consumer_key=consumer_key,
            consumer_secret=consumer_secret)

        self.ox.logon(email, password)

        logger.info('OX Logged on')

    def get_lookup_data(self):
        emails = dict()
        
        for name in self.DATA_TYPES:
            
            # Get this model
            model = getattr(spendata.models, 'OpenX{name}'.format(name=name.capitalize()))
            
            data_ids = self.ox.get('/a/{name}'.format(name=name))
            logger.info('Retrieved {} IDs for {}'.format(len(data_ids), name))
            
            for data_id in data_ids:
                
                data = self.ox.get('/a/{name}/{id}'.format(name=name, id=data_id))
                
                logger.debug('Raw data')
                logger.debug(data)
                parsed_data = parse_data(data, self._parsers, name)
                logger.debug('Parsed data')
                logger.debug(parsed_data)
                
                #For OpenXUser, keep a record of unique emails
                logger.info("downloading table {}".format(name))
                if name == "user": 
                    email = parsed_data["email"]
                    logger.info("email = {}".format(email))
                    if not email in emails:
                        emails[email] = '1'
                        logger.info("email {} is new, inserting".format(email))
                        spendata.models.OpenXUserEmail.objects.get_or_create(email=email)                
                
                
                obj, created = model.objects.get_or_create(id=data_id, defaults=parsed_data)
                if created == False:
                    logger.debug('Updating ' + name + ' id=' + str(data_id) )
                    for attr in parsed_data:
                        val = parsed_data[attr]
                        #logger.debug('setting attribute:' + attr + '=' + str(val) )
                        if hasattr(obj, attr):
                            setattr(obj, attr, val)
                    #logger.debug('obj after updates')
                    #logger.debug(obj)
                    obj.save(force_update=True)
                
    
    def get_model_code(self):
        """ Prints class definitions and stores how to parse each data field """
        
        for name in self.DATA_TYPES:
            print '\n\nclass OpenX{}(models.Model):'.format(name.capitalize())
            
            fields = self.ox.get('/a/{name}/availableFields?action=create'.format(name=name))
            
            for field_name, field_data in fields.iteritems():
                
                field = DataField(field_data['type'])
                
                print '    {field_name:<25} = models.{field_type}({options})'.format(
                    field_name = field_name,
                    field_type = field.type,
                    options    = field.options
                )
                
                self._parsers[name][field_name] = field.parser
    
    @classmethod
    def get_serializer_code(cls):
        
        for name in cls.DATA_TYPES:
            print """
class OpenX{0}Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OpenX{0}""".format(name.capitalize())
        
        
    @classmethod
    def get_views_code(cls):

        for name in cls.DATA_TYPES:
            print """
class OpenX{0}ViewSet(viewsets.ModelViewSet):
    queryset = OpenX{0}.objects.all()
    serializer_class = OpenX{0}Serializer""".format(name.capitalize())

    @classmethod
    def get_url_code(cls):

        for name in cls.DATA_TYPES:
            print "router.register(r'openx_{}', views.OpenX{}ViewSet)".format(name.lower(), name.capitalize())


def parse_data(data, parsers, name):
    
    parsed_data = {}
    
    for dname, value in data.iteritems():
        
        try:
            parsed_data[dname] = parsers[name][dname](value)
        except TypeError:
            parsed_data[dname] = None
            
        except Exception as e:
            print dname, name, value
            print data
    
    return parsed_data

def strip_brackets(field):
    """ Strips out brackets and numbers - e.g. varchar(200) -> varchar, decimal(20,5) -> decimal"""
    try:
        return re.match('(.+)\(\d+,{0,1}\d*\)', field).groups()[0]
    except AttributeError:
        return field


class DataField(object):
    def parse_datetime(string):
        return dateutil.parser.parse(string)
    
    # Data field types - e.g. string: TextField
    TEXTFIELD = ('TextField', 'blank=True', lambda x: '' if x is None else x)
    FIELD_TYPES = {
        'int':        ('IntegerField', 'null=True, blank=True', int),
        'bigint':     ('BigIntegerField', 'null=True, blank=True', long),
        'datetime':   ('DateTimeField', 'null=True, blank=True', parse_datetime),
        'timestamp':  ('DateTimeField', 'null=True, blank=True', parse_datetime),
        'string':     TEXTFIELD,
        'varchar':    TEXTFIELD,
        'varbinary':  TEXTFIELD,
        'mediumtext': TEXTFIELD,
        'email':      TEXTFIELD,
        'ids':        TEXTFIELD, # ??
        'url':        TEXTFIELD,
        'decimal':    ('DecimalField', 'max_digits={}, decimal_places={}, null=True, blank=True', decimal.Decimal)
    }
    
    def __init__(self, rawfieldtype):
    
        field_data_type = strip_brackets(rawfieldtype)
        field_type, field_options, field_parser = self.FIELD_TYPES.get(field_data_type, (None, None, None))
    
        # Unknown field type
        if field_type is None:
            print 'MISSING FIELD TYPE: {} {}'.format(field_name, field_data)
            return None
        
        # Decimal field (fixed decimal precision)
        if field_data_type == 'decimal':                    
            one, two = rawfieldtype.replace('decimal(', '').replace(')','').split(',')
            field_options = field_options.format(one, two)
        
        self.type = field_type
        self.options = field_options
        self.parser = field_parser
