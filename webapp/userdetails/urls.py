# __author__ = 'sumeet'
from django.conf.urls import include, url
from django.contrib import admin
from . import views



urlpatterns = [
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'userdetails.views.Login()')
    url(r'^$',(views.Login.as_view())),
]