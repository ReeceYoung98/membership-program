from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^users/$', views.allusers, name='allusers'),
	url(r'^users/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
]