from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.data_upload, name='data_upload'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^predict/',views.prediction,name='predection')

    ]