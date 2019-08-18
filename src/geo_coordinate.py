import math

from src.bounding_box import EARTH_RADIUS


class GeoCoordinate:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.latitude_in_rad = math.radians(latitude)
        self.longitude = longitude
        self.longitude_in_rad = math.radians(longitude)

    def distance_in_km_from(self, other):
        # Haversine formula
        delta_lon = other.longitude_in_rad - self.longitude_in_rad
        delta_lat = other.latitude_in_rad - self.latitude_in_rad
        square_of_half_the_chord_length = math.sin(delta_lat / 2) ** 2 + math.cos(self.latitude_in_rad) * math.cos(
            other.latitude_in_rad) * math.sin(delta_lon / 2) ** 2
        angular_distance_in_rad = 2 * math.asin(math.sqrt(square_of_half_the_chord_length))
        return angular_distance_in_rad * EARTH_RADIUS
