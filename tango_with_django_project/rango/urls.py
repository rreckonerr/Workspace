from django.conf.urls import url
from rango import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^about', views.about, name='about')
]