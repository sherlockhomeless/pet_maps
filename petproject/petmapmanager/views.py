from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import Location, County, Animal
from django.core.serializers import serialize


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


def LocationData(request):
    points = serialize('geojson', Location.objects.all())
    return HttpResponse(points, content_type='json')


def CountyData(request):
    counties = serialize('geojson', County.objects.all())
    return HttpResponse(counties, content_type='json')


def AnimalData(request):
    animals = serialize('geojson', Animal.objects.all())
    return HttpResponse(animals, content_type='json')
