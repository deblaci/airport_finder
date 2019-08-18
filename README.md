# World of Airports

It's a python3 app that retrieves airports within a user provided radius(in km) of user provided lat/long point.

## Installation

Python 3.7.2 need to be installed to run.
Use the package manager [pip](https://github.com/cloudant/python-cloudant) to install cloudant.

```bash
pip install cloudant
```


## Usage

```bash
python airport_finder.py --lat=<latitude> --lon=<longitude> --rad=<radius in km>

Example:
python airport_finder.py --lat=47.503665 --lon=19.0592053 --rad=50
```
