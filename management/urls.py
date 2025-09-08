"""
URL configuration for airline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.urls import path

from management.views import (
    index,
    FlightListView,
    StaffListView,
    PlaneListView,
    AirportListView,
    AirportDetailView,
    PlaneDetailView,
    StaffDetailView,
    FlightDetailView, AirportCreateView, PlaneCreateView, StaffCreateView, FlightCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("airports/", AirportListView.as_view(), name="airports"),
    path("airports/<int:pk>/", AirportDetailView.as_view(), name="airport-detail"),
    path("airports/create/", AirportCreateView.as_view(), name="airport-create"),
    path("planes/", PlaneListView.as_view(), name="planes"),
    path("planes/<int:pk>/", PlaneDetailView.as_view(), name="plane-detail"),
    path("planes/create/", PlaneCreateView.as_view(), name="plane-create"),
    path("staff/", StaffListView.as_view(), name="staff"),
    path("staff/<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),
    path("staff/create/", StaffCreateView.as_view(), name="staff-create"),
    path("flights/", FlightListView.as_view(), name="flights"),
    path("flights/<int:pk>/", FlightDetailView.as_view(), name="flight-detail"),
    path("flights/create/", FlightCreateView.as_view(), name="flight-create"),
]

app_name = "management"
