from django.conf.urls import url
from .views import all_bugs, thread, submit_bug

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^thread/(?P<bug_id>\w{0,50})/$', thread, name='thread'),
    url(r'^submit_bug/$', submit_bug, name='submit_bug'),
]