from django.db import models

class OpenXAccount(models.Model):
    primary_contact_id        = models.IntegerField(null=True)
    blocked_creativetypes     = models.TextField(null=True)
    ac_account_id             = models.IntegerField(null=True)
    total_impressions         = models.IntegerField(null=True)
    account_manager_id        = models.IntegerField(null=True)
    currency_id               = models.IntegerField(null=True)
    brands                    = models.TextField(null=True)
    filters                   = models.TextField(null=True)
    uplift                    = models.IntegerField(null=True)
    modified_date             = models.DateTimeField()
    sales_lead_id             = models.IntegerField(null=True)
    country_of_business_id    = models.TextField(null=True)
    blocked_contentattributes = models.TextField(null=True)
    blocked_languages         = models.TextField(null=True)
    clicks                    = models.IntegerField(null=True)
    allow_unbranded_buyers    = models.IntegerField(null=True)
    status                    = models.TextField(null=True)
    fill_rate                 = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    exchange                  = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    buyer_breakout            = models.IntegerField(null=True)
    market_active             = models.IntegerField(null=True)
    single_ad_limitation      = models.IntegerField(null=True)
    account_type_id           = models.IntegerField(null=True)
    market_currency_id        = models.IntegerField(null=True)
    brand_labels              = models.TextField(null=True)
    name                      = models.TextField(null=True)
    timezone_id               = models.IntegerField(null=True)
    notes                     = models.TextField(null=True)
    total_conversions         = models.IntegerField(null=True)
    instance_id               = models.IntegerField(null=True)
    blocked_adcategories      = models.TextField(null=True)
    billing_contact_id        = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    domains                   = models.TextField(null=True)
    requests                  = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)


class OpenXUser(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    first_name                = models.TextField(null=True)
    last_name                 = models.TextField(null=True)
    verified                  = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    roles                     = models.TextField(null=True)
    locale                    = models.TextField(null=True)
    notes                     = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    default_report_range      = models.TextField(null=True)
    terms_accepted            = models.DateTimeField()
    created_date              = models.DateTimeField()
    external_id               = models.TextField(null=True)
    email                     = models.TextField(null=True)


class OpenXRole(models.Model):
    modified_date             = models.DateTimeField()
    name                      = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    acl_uid                   = models.TextField(null=True)
    system                    = models.IntegerField(null=True)
    compiled_acl              = models.TextField(null=True)
    created_date              = models.DateTimeField()
    account_id                = models.IntegerField(null=True)


class OpenXSite(models.Model):
    filters                   = models.TextField(null=True)
    domain_override           = models.TextField(null=True)
    blocked_creativetypes     = models.TextField(null=True)
    category_override         = models.IntegerField(null=True)
    modified_date             = models.DateTimeField()
    content_topic_id          = models.IntegerField(null=True)
    blocked_contentattributes = models.TextField(null=True)
    blocked_languages         = models.TextField(null=True)
    allow_unbranded_buyers    = models.IntegerField(null=True)
    status                    = models.TextField(null=True)
    account_id                = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    brands                    = models.TextField(null=True)
    name                      = models.TextField(null=True)
    brand_labels              = models.TextField(null=True)
    content_type_id           = models.IntegerField(null=True)
    url                       = models.TextField(null=True)
    notes                     = models.TextField(null=True)
    platform_id               = models.TextField(null=True)
    blocked_adcategories      = models.TextField(null=True)
    created_date              = models.DateTimeField()
    domains                   = models.TextField(null=True)
    external_id               = models.TextField(null=True)


class OpenXAdunit(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    sitesection_id            = models.IntegerField(null=True)
    name                      = models.TextField(null=True)
    content_type_id           = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)
    site_id                   = models.IntegerField(null=True)
    alt_sizes                 = models.TextField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    vast_tag                  = models.TextField(null=True)
    created_date              = models.DateTimeField()
    content_topics            = models.TextField(null=True)
    primary_size              = models.TextField(null=True)
    real_time_bid_floor       = models.DecimalField(max_digits=9, decimal_places=2)
    account_id                = models.IntegerField(null=True)


class OpenXAdunitgroup(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    adunits                   = models.TextField(null=True)
    name                      = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    description               = models.TextField(null=True)
    site_id                   = models.IntegerField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    vast_tag                  = models.TextField(null=True)
    created_date              = models.DateTimeField()
    masteradunit_id           = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)
    account_id                = models.IntegerField(null=True)


class OpenXOrder(models.Model):
    status                    = models.TextField(null=True)
    booking_account_id        = models.IntegerField(null=True)
    sales_lead_id             = models.IntegerField(null=True)
    primary_trafficker_id     = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    end_date                  = models.DateTimeField()
    click_through_window      = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    notes                     = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    budget                    = models.DecimalField(max_digits=11, decimal_places=2)
    secondary_trafficker_id   = models.IntegerField(null=True)
    primary_analyst_id        = models.IntegerField(null=True)
    creator_id                = models.IntegerField(null=True)
    single_ad_limitation      = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    view_through_window       = models.IntegerField(null=True)
    external_id               = models.TextField(null=True)
    start_date                = models.DateTimeField()
    name                      = models.TextField(null=True)


class OpenXLineitem(models.Model):
    pricing_model_id          = models.IntegerField(null=True)
    lifetime_impression_cap   = models.IntegerField(null=True)
    lifetime_click_cap        = models.IntegerField(null=True)
    companion_fill_method_id  = models.IntegerField(null=True)
    deliver_by_default        = models.IntegerField(null=True)
    daily_click_cap           = models.IntegerField(null=True)
    modified_date             = models.DateTimeField()
    make_good                 = models.IntegerField(null=True)
    ad_delivery_id            = models.IntegerField(null=True)
    share_of_voice            = models.DecimalField(max_digits=3, decimal_places=1)
    lifetime_action_cap       = models.IntegerField(null=True)
    pacing_model_id           = models.IntegerField(null=True)
    priority                  = models.IntegerField(null=True)
    deleted                   = models.IntegerField(null=True)
    buying_model_id           = models.IntegerField(null=True)
    daily_impression_goal     = models.BigIntegerField(null=True)
    start_date                = models.DateTimeField()
    status                    = models.TextField(null=True)
    session_duration          = models.IntegerField(null=True)
    account_id                = models.IntegerField(null=True)
    end_date                  = models.DateTimeField()
    order_id                  = models.IntegerField(null=True)
    targeting_rules           = models.TextField(null=True)
    session_display_cap       = models.IntegerField(null=True)
    delivery_medium_id        = models.IntegerField(null=True)
    individual_display_cap    = models.IntegerField(null=True)
    lifetime_impression_goal  = models.BigIntegerField(null=True)
    daily_impression_cap      = models.IntegerField(null=True)
    budget_type               = models.TextField(null=True)
    single_ad_limitation      = models.IntegerField(null=True)
    name                      = models.TextField(null=True)
    pricing_rate              = models.DecimalField(max_digits=11, decimal_places=4)
    oxtl                      = models.TextField(null=True)
    notes                     = models.TextField(null=True)
    created_date              = models.DateTimeField()
    external_id               = models.TextField(null=True)


class OpenXAd(models.Model):
    status                    = models.TextField(null=True)
    modified_date             = models.DateTimeField()
    days_of_week              = models.TextField(null=True)
    session_duration          = models.IntegerField(null=True)
    hours_of_day              = models.TextField(null=True)
    name                      = models.TextField(null=True)
    end_date                  = models.DateTimeField()
    deliver_by_default        = models.IntegerField(null=True)
    order_id                  = models.IntegerField(null=True)
    creative_id               = models.IntegerField(null=True)
    ad_weight                 = models.DecimalField(max_digits=3, decimal_places=1)
    deleted                   = models.IntegerField(null=True)
    session_display_cap       = models.IntegerField(null=True)
    ad_type_id                = models.IntegerField(null=True)
    individual_display_cap    = models.IntegerField(null=True)
    notes                     = models.TextField(null=True)
    lineitem_id               = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    external_id               = models.TextField(null=True)
    start_date                = models.DateTimeField()
    account_id                = models.IntegerField(null=True)


class OpenXCreative(models.Model):
    file2                     = models.TextField(null=True)
    account_id                = models.IntegerField(null=True)
    source                    = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    bitrate                   = models.DecimalField(max_digits=10, decimal_places=2)
    notes                     = models.TextField(null=True)
    created_date              = models.DateTimeField()
    modified_date             = models.DateTimeField()
    uri                       = models.TextField(null=True)
    height                    = models.IntegerField(null=True)
    ad_type_id                = models.IntegerField(null=True)
    width                     = models.IntegerField(null=True)
    orig_name                 = models.TextField(null=True)
    file                      = models.TextField(null=True)
    file_size                 = models.DecimalField(max_digits=11, decimal_places=2)
    duration                  = models.DecimalField(max_digits=10, decimal_places=2)
    external_id               = models.TextField(null=True)
    mime_type                 = models.TextField(null=True)
    name                      = models.TextField(null=True)


class OpenXRule(models.Model):
    modified_date             = models.DateTimeField()
    deleted                   = models.IntegerField(null=True)
    attribute                 = models.TextField(null=True)
    value                     = models.TextField(null=True)
    lineitem_id               = models.IntegerField(null=True)
    created_date              = models.DateTimeField()
    operator                  = models.TextField(null=True)
    external_id               = models.TextField(null=True)
    dimension                 = models.TextField(null=True)


class OpenXReport(models.Model):
    modified_date             = models.DateTimeField()
    user_id                   = models.IntegerField(null=True)
    name                      = models.TextField(null=True)
    deleted                   = models.IntegerField(null=True)
    parameter_string          = models.TextField(null=True)
    created_date              = models.DateTimeField()
    relative_date             = models.TextField(null=True)