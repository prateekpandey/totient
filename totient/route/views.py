from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Route
from .serializer import RouteSerializer, LocationSerializer


class RouteListCreateAPIView(generics.ListCreateAPIView):
	serializer_class = RouteSerializer

	def get_queryset(self):
		return Route.objects.filter(user=self.request.user)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.auth_user = self.request.user
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LocationCreateAPIView(generics.CreateAPIView):
	serializer_class = LocationSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data, many=True)
		serializer.auth_user = self.request.user
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AdminRouteListAPIView(generics.ListAPIView):
	serializer_class = RouteSerializer
	permission_classes = (permissions.IsAdminUser, )

	def get_queryset(self):
		return Route.objects.all()

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())

		user_id = request.query_params.get('user', None)
		date_from = request.query_params.get('date_from', None)
		date_till = request.query_params.get('date_till', None)

		if user_id:
			queryset = queryset.filter(user_id=user_id)

		if date_from:
			kwargs['date__gte'] = date_from
		if date_till:
			kwargs['date__lte'] = date_till
		if kwargs:
			queryset.filter(**kwargs)
		else:
			queryset = [queryset.latest('date')] if queryset else None

		page = self.paginate_queryset(queryset)
		if page is not None:
			serializer = self.get_serializer(page, many=True)
			return self.get_paginated_response(serializer.data)

		serializer = self.get_serializer(queryset, many=True)
		return Response(serializer.data)


