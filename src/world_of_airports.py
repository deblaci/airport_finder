from src.bounding_box import BoundingBox
from src.geo_coordinate import GeoCoordinate
from src.query_client import QueryClient


class WorldOfAirports:
    def __init__(self, latitude, longitude, radius):
        self.point = GeoCoordinate(latitude, longitude)
        self.radius = radius
        self.airports = {}
        self.query = QueryClient()

    def airports_within_radius(self):
        bounding_box = BoundingBox(self.point, self.radius)
        self.filter_circle(self.query.airports_inside(bounding_box.list()))

    def filter_circle(self, airports):
        for row in airports:
            distance = self.point.distance_in_km_from(GeoCoordinate(row['fields']['lat'], row['fields']['lon']))
            if distance <= self.radius:
                self.airports[distance] = row

    def print_ariport_list(self):
        print("Result:")
        if not self.airports:
            print("The airport list is empty.")
        for key in sorted(self.airports.keys()):
            print("%skm, %s(lat: %s, lon: %s)" % (
                round(key, 1), self.airports[key]['fields']['name'], self.airports[key]['fields']['lat'],
                self.airports[key]['fields']['lon']))
