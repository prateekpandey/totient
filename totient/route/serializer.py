import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers, exceptions

from .service import calculate_distance
from .models import Route, Location


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location

	def is_valid(self, raise_exception=False):
		if self.initial_data['location'].user != self.auth_user:
			raise exceptions.ValidationError("Route does not belongs to logged in user")
		return super().is_valid(raise_exception)


class RouteSerializer(serializers.ModelSerializer):
	locations = LocationSerializer(many=True, read_only=True)
	date = serializers.DateField(default=datetime.date.today)
	distance = serializers.SerializerMethodField()

	class Meta:
		model = Route

	def get_distance(self, value):
		locations = value.locations.all()
		if not locations:
			return 0
		prev_location = locations[0]
		distance = 0
		for location in locations[1:]:
			distance += calculate_distance(prev_location.lat, prev_location.long, location.lat, location.long)
			prev_location = location
		return distance

	def is_valid(self, raise_exception=False):
		self.initial_data['user'] = self.auth_user.pk
		return super().is_valid(raise_exception)
