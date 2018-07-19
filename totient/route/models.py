import datetime

from django.db import models
from django.conf import settings


class Route(models.Model):
	name = models.CharField(max_length=50, help_text="Route title or subject or purpose")
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	date = models.DateField()

	class Meta:
		unique_together = ('user', 'date')

	# def save(self, **kwargs):
	# 	if not self.date:
	# 		self.date = datetime.date.today()
	# 	return super().save(**kwargs)


class Location(models.Model):
	lat = models.FloatField(help_text='ranges from -90 to +90')
	long = models.FloatField(help_text='ranges from -180 to 180')
	route = models.ForeignKey(Route, related_name='locations')
