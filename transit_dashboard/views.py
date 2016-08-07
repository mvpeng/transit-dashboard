from django.shortcuts import render
import googlemaps
from datetime import datetime
import os

gmaps = googlemaps.Client(key=os.environ.get('TRANSITDASH_GOOGLE_SECRET'))

def index(request):
    result = gmaps.distance_matrix("542 Green St, San Francisco, CA 94133", 
                                         "700 4th St, San Francisco, CA 94107",
                                         mode="transit",
                                         departure_time=datetime.now())
    return render(request, 'index.html', {'result': result})