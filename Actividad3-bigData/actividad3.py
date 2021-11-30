"""
Example of dot density map
"""
import geoplotlib
from geoplotlib.utils import read_csv


data = read_csv('bus.csv')
geoplotlib.dot(data)
geoplotlib.show()
