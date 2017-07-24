from django.conf.urls import url
from django.contrib.auth.views import login
from .views import logout, signup

urlpatterns = [
    url(r'^login/', login, name='login', kwargs={'template_name': 'account/login.html'}),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', signup, name='signup'),
]
