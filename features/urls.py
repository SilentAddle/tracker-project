from django.conf.urls import url
from .views import all_features, thread, submit_feature, updoot_feature

urlpatterns = [
    url(r'^$', all_features, name='features'),
    url(r'^thread/(?P<feature_id>\w{0,50})/$', thread, name='thread'),
    url(r'^submit_feature/$', submit_feature, name='submit_feature'),
    url(r'^updoot_feature/$', updoot_feature, name='updoot_feature'),
]