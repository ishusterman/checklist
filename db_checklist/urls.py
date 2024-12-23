from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
    #url(r'^$' , views.cool_view, name='cool_view'),
    #url(r'^$', views.index, name='index'),d

    url(r'^(?P<id>[0-9]+)/$', views.index, name='index'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^test_model/(?P<id>[0-9]+)/$', views.get_ChecklistForm, name='get_ChecklistForm'),
    url(r'^save/', views.save, name='save'),
    url(r'^save_model/', views.save_model, name='save_model'),
    url(r'^logoff/', views.logoff, name='logoff'),
    url(r'^password_change/', include('django.contrib.auth.urls')),
    url(r'^$', views.cool_view, name='cool_view'),

]