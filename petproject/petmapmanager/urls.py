from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('locations/', LocationData, name='locations'),
    path('counties/', CountyData, name='counties'),
    path('animals/', AnimalData, name='animals'),
]
