from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index), 
	url(r'^index$', views.mainother),
	# url(r'^edit$', views.edit),
	url(r'^notes/(\d+)$', views.notecontent),
	url(r'^login$', views.login),
	url(r'^user/(\d{13})$', views.userspace)

]