from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from management.models import (
    Airport,
    Plane,
    Staff,
    Flight
)


# Create your views here.

@login_required
def index(request):
    num_airports = Airport.objects.count()
    num_planes = Plane.objects.count()
    num_staff = Staff.objects.count()
    num_flights = Flight.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_airports": num_airports,
        "num_planes": num_planes,
        "num_staff": num_staff,
        "num_flights": num_flights,
        "num_visits": num_visits,
    }

    return render(request, "management/index.html", context=context)


class AirportListView(LoginRequiredMixin, generic.ListView):
    model = Airport
    paginate_by = 5


class PlaneListView(LoginRequiredMixin, generic.ListView):
    model = Plane
    paginate_by = 5


class FlightListView(LoginRequiredMixin, generic.ListView):
    model = Flight
    paginate_by = 5


class StaffListView(LoginRequiredMixin, generic.ListView):
    model = Staff
    paginate_by = 5