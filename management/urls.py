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
    FlightDetailView,
    AirportCreateView,
    PlaneCreateView,
    StaffCreateView,
    FlightCreateView,
    AirportUpdateView,
    PlaneUpdateView,
    StaffUpdateView,
    FlightUpdateView,
    AirportDeleteView,
    PlaneDeleteView,
    StaffDeleteView,
    FlightDeleteView,
    toggle_assign_to_plane,
    toggle_assign_to_airport,
    change_password
)


urlpatterns = [
    path("", index, name="index"),
    path("airports/", AirportListView.as_view(), name="airports"),
    path("airports/<int:pk>/", AirportDetailView.as_view(), name="airport-detail"),
    path("airports/create/", AirportCreateView.as_view(), name="airport-create"),
    path("airports/<int:pk>/update/", AirportUpdateView.as_view(), name="airport-update"),
    path("airports/<int:pk>/delete/", AirportDeleteView.as_view(), name="airport-delete"),
    path("planes/", PlaneListView.as_view(), name="planes"),
    path("planes/<int:pk>/", PlaneDetailView.as_view(), name="plane-detail"),
    path("planes/create/", PlaneCreateView.as_view(), name="plane-create"),
    path("planes/<int:pk>/update/", PlaneUpdateView.as_view(), name="plane-update"),
    path("planes/<int:pk>/delete/", PlaneDeleteView.as_view(), name="plane-delete"),
    path("staff/", StaffListView.as_view(), name="staff"),
    path("staff/<int:pk>/", StaffDetailView.as_view(), name="staff-detail"),
    path("staff/create/", StaffCreateView.as_view(), name="staff-create"),
    path("staff/<int:pk>/update/", StaffUpdateView.as_view(), name="staff-update"),
    path("staff/<int:pk>/delete/", StaffDeleteView.as_view(), name="staff-delete"),
    path("flights/", FlightListView.as_view(), name="flights"),
    path("flights/<int:pk>/", FlightDetailView.as_view(), name="flight-detail"),
    path("flights/create/", FlightCreateView.as_view(), name="flight-create"),
    path("flights/<int:pk>/update", FlightUpdateView.as_view(), name="flight-update"),
    path("flights/<int:pk>/delete/", FlightDeleteView.as_view(), name="flight-delete"),
    path("planes/<int:pk>/toggle/", toggle_assign_to_plane, name="toggle-assign-to-plane"),
    path("airports/<int:pk>/toggle/", toggle_assign_to_airport, name="toggle-assign-to-airport"),
    path("staff/<int:pk>/password", change_password, name="password")
]
app_name = "management"
