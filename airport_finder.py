#!/usr/bin/python
import argparse
import sys

from src.world_of_airports import WorldOfAirports

LONGITUDE_MAX = 180
LATITUDE_MAX = 90


def main(argv):
    parser = argparse.ArgumentParser()
    try:
        parser.add_argument('-a', '--lat', help="base point latitude value in (-90, 90) degree", required=True,
                            type=float)
        parser.add_argument('-o', '--lon', help="base point longitude value in (-180, 180) degree", required=True,
                            type=float)
        parser.add_argument('-r', '--rad', help="radius in km > 0", required=True, type=float)
        args = parser.parse_args()
        boundary_check(args)

        latitude = float(args.lat)
        longitude = float(args.lon)
        radius = float(args.rad)
    except ValueError as e:
        print(e)
        parser.print_help()
        sys.exit(1)

    wa = WorldOfAirports(latitude, longitude, radius)
    wa.airports_within_radius()
    wa.print_ariport_list()


def boundary_check(args):
    if args.lat > LATITUDE_MAX or args.lat < -LATITUDE_MAX:
        raise ValueError('latitude is out of range: %s' % (args.lat))
    if args.lon > LONGITUDE_MAX or args.lon < -LONGITUDE_MAX:
        raise ValueError('longitude is out of range: %s' % (args.lon))
    if args.rad <= 0:
        raise ValueError('radius is less than or equal to zero: %s' % (args.rad))


if __name__ == "__main__":
    main(sys.argv[1:])
