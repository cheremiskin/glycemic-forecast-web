from django.urls import path

from . import views

urlpatterns = [
    path('glycemic-forecast', views.glycemic_forecast, name='glycemic_forecast'),
]
