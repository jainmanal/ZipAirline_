from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('fuel-details',views.Index,name="fuel_details")
]
