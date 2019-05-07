from django.conf.urls import url
from .views import all_bugs, thread, submit_bug, updoot_bug

urlpatterns = [
    url(r'^$', all_bugs, name='bugs'),
    url(r'^bug-thread/(?P<bug_id>\w{0,50})/$', thread, name='bug-thread'),
    url(r'^submit_bug/$', submit_bug, name='submit_bug'),
    url(r'^updoot_bug/$', updoot_bug, name='updoot_bug'),
]