from math import sin, cos, sqrt, atan2, radians


def calculate_distance(lat1, long1, lat2, long2):
	"""
	Calculates distance between 2 points (lat1, long1) => (lat2, long2)
	Returns: Distance in kms
	"""
	earth_radius = 6373.0
	lat1, long1, lat2, long2 = list(map(radians, (lat1, long1, lat2, long2)))
	dlon = long2 - long1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	return earth_radius * c