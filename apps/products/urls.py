from django.conf.urls import url
from apps.products import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^create$', views.create),
	url(r'^destroy/(?P<id>\d+)$', views.destroy),
	url(r'^show/(?P<id>\d+)$', views.show),
	url(r'^update/(?P<id>\d+)$', views.update),
]
