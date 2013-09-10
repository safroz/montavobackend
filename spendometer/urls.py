from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from spendata import views


# REST API stuff
router = routers.DefaultRouter()

# no need for these at the moment
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'acxiom', views.AcxiomDataViewSet)
router.register(r'mobile_user', views.MobileAppUserDataViewSet)
router.register(r'mobile_data', views.MobileAppMobileDataViewSet)
router.register(r'mobile_location', views.MobileAppLocationDataViewSet)

router.register(r'openx_account', views.OpenXAccountViewSet)
router.register(r'openx_user', views.OpenXUserViewSet)
router.register(r'openx_role', views.OpenXRoleViewSet)
router.register(r'openx_site', views.OpenXSiteViewSet)
router.register(r'openx_adunit', views.OpenXAdunitViewSet)
router.register(r'openx_adunitgroup', views.OpenXAdunitgroupViewSet)
router.register(r'openx_order', views.OpenXOrderViewSet)
router.register(r'openx_lineitem', views.OpenXLineitemViewSet)
router.register(r'openx_ad', views.OpenXAdViewSet)
router.register(r'openx_creative', views.OpenXCreativeViewSet)
router.register(r'openx_rule', views.OpenXRuleViewSet)
router.register(r'openx_report', views.OpenXReportViewSet)

# Admin stuff
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
    url(r'^', include(router.urls)),
)