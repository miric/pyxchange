from django.conf.urls import url
from . import views

app_name = 'pyxchange'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^popular/$', views.show_popular, name='popular'),
    url(r'^all/$', views.show_all, name='all'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^user/$', views.cabinet, name='cabinet'),
    url(r'^(?P<slug>[\w]+)/$', views.detail, name='detail'),
    # url(r'^(?P<slug>[\w]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<slug>[\w]+)/delete/$', views.ImageDelete.as_view(), name='delete'),
]
