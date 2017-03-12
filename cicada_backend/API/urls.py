from django.conf.urls import url,include
from django.contrib import admin
from cicada_backend.API.views import *


urlpatterns = [
    url(r'^user-profile/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^user-profile/$', UserList.as_view()),

    url(r'^notification/$',NotificationManager.as_view()),
    url(r'^notification/(?P<pk>[0-9]+)/$',NotificationDetail.as_view()),

    url(r'^organization/$', OrganizationList.as_view()),
    url(r'^organization/(?P<pk>[0-9]+)/$', OrganizationDetail.as_view()),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'^mobile/user/$',UserProfileManager.as_view()),

    url(r'^mobile/component/', ComponentManager.as_view()),

    url(r'^mobile/response/$',UserResponseManager.as_view()),
    url(r'^mobile/response/(?P<pk>[0-9]+)/$', UserResponseManager.as_view()),

    url(r'^test/',testApi.as_view()),
]