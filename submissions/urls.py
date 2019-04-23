from django.conf.urls import url, include
from .views import all_submissions
    
urlpatterns = [
    url(r'^$', all_submissions, name='submissions')
]