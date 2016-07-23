from django.conf.urls import url
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'members'

urlpatterns = [
    url(r'^$', views.anonymous_required(views.LoginFormView.as_view()), name='login_form'),
    url(r'^register/$', views.anonymous_required(views.RegisterFormView.as_view()), name='register_form'),
    url(r'^users/$', login_required(views.allusers), name='allusers'),
    url(r'^users/(?P<user_id>[0-9]+)/$', login_required(views.profile), name='profile'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
]
