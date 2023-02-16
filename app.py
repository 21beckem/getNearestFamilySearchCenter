!pip install googlemaps
import googlemaps
gmaps = googlemaps.Client(key=API_key)
origin = (LatOrigin, LongOrigin)
destination = (LatDestination, LongDestination)
result = gmaps.distance_matrix(origin, destination, mode = 'driving')
result_distance = result["rows"][0]["elements"][0]["distance"]["value"]
result_time = result["rows"][0]["elements"][0]["duration"]["value"]
