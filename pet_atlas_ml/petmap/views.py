from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import County, PinLocation

from django.core.serializers import serialize

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class LocationData(request):
    points = serialize('geojson', PinLocation.objects.all())
    return HttpResponse(points, content_type='json')

class CountyData(request):
    points = serialize('geojson', County.objects.all())
    return HttpResponse(points, content_type='json')
