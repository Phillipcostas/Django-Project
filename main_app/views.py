from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse('<h1>Hello ᓚᘏᗢ<h1>')

def calendar(request):
    return render(request, 'calendar.html')

def itinerary(request):
    return render(request, 'itinerary.html', {'itinerary': itinerary})


class itinerary:
    def __init__ (self, item, date, description,):
        self.item = item
        self.date = date
        self.description = description 

itinerary = [
    itinerary('hike', 12/12/2024, 'mountain hike'),
    itinerary('hike', 12/12/2024, 'mountain hike'),
    itinerary('hike', 12/12/2024, 'mountain hike'),
]