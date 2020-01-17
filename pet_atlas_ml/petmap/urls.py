from django.contrib import admin
from django.urls import path, include
from .views import HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('', include('pet_atlas_ml'))

]
