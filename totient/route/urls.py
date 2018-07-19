from django.conf.urls import url
from .import views

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	url(r'^routes/$', views.RouteListCreateAPIView.as_view(), name='route-list'),
	url(r'^locations/$', views.LocationCreateAPIView.as_view(), name='route-list'),

	url(r'^admin/routes/$', views.AdminRouteListAPIView.as_view(), name='route-list'),

	# url(r'^api-token-auth/', obtain_jwt_token),
]
