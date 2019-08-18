import copy
import math

EARTH_RADIUS = 6371  # in km
NORTH_POLE = 90
SOUTH_POLE = -90
MERIDIAN_180TH = 180
LONGITUDE_BOUNDARY = 360


class BoundingBox:
    def __init__(self, point, radius):
        self.longitude_min = point.longitude - math.degrees(
            math.asin(radius / EARTH_RADIUS) / math.cos(point.latitude_in_rad))
        self.longitude_max = point.longitude + math.degrees(
            math.asin(radius / EARTH_RADIUS) / math.cos(point.latitude_in_rad))
        self.longitude_out_of_range()

        self.latitude_min = point.latitude - math.degrees(radius / EARTH_RADIUS)
        self.latitude_max = point.latitude + math.degrees(radius / EARTH_RADIUS)
        self.poles_in_latitude()

    def longitude_out_of_range(self):
        if self.longitude_min < -MERIDIAN_180TH:
            self.longitude_min += LONGITUDE_BOUNDARY
        if self.longitude_max > MERIDIAN_180TH:
            self.longitude_max -= LONGITUDE_BOUNDARY

    def poles_in_latitude(self):
        if self.latitude_max >= NORTH_POLE or self.latitude_min < SOUTH_POLE:
            self.latitude_min = max(self.latitude_min, SOUTH_POLE)
            self.latitude_max = min(self.latitude_max, NORTH_POLE)
            self.longitude_min = -MERIDIAN_180TH
            self.longitude_max = MERIDIAN_180TH

    def list(self):
        """
        Retrieves a list of bounding boxes. Two box required when box point would be out of longitude range.
        :returns: List of bounding boxes
        """
        # if max < min, two bounding box need to cover the area
        if self.longitude_max < self.longitude_min:
            left_box = copy.deepcopy(self)
            right_box = copy.deepcopy(self)
            left_box.longitude_min = -MERIDIAN_180TH
            left_box.longitude_max = self.longitude_max
            right_box.longitude_min = self.longitude_min
            right_box.longitude_max = MERIDIAN_180TH
            return [left_box, right_box]
        return [self]
