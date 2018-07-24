import googlemaps
from datetime import datetime


def google(text):
	gmaps = googlemaps.Client(key='AIzaSyCcgY4MwelgM_TGBsyELyHxkDQ30GNnWAM')
	#gmaps = googlemaps.Client(key='AIzaSyDWqgDyEf7Vk4pURXc4mLQEeIFsLqRD-KI')
	geocode_result = gmaps.geocode(text)
	return geocode_result
