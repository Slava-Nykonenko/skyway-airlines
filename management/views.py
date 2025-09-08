from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from management.forms import (
    AirportForm,
    PlaneForm,
    FlightForm,
    StaffForm)
from management.models import (
    Airport,
    Plane,
    Flight,
    Staff
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


class AirportDetailView(LoginRequiredMixin, generic.DetailView):
    model = Airport


class AirportCreateView(LoginRequiredMixin, generic.CreateView):
    model = Airport
    form_class = AirportForm
    success_url = reverse_lazy("management:airports")


class AirportUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Airport
    form_class = AirportForm
    success_url = reverse_lazy("management:airports")


class AirportDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Airport
    success_url = reverse_lazy("management:airports")


class PlaneListView(LoginRequiredMixin, generic.ListView):
    model = Plane
    paginate_by = 5


class PlaneDetailView(LoginRequiredMixin, generic.DetailView):
    model = Plane


class PlaneCreateView(LoginRequiredMixin, generic.CreateView):
    model = Plane
    form_class = PlaneForm
    success_url = reverse_lazy("management:planes")


class PlaneUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Plane
    form_class = PlaneForm
    success_url = reverse_lazy("management:planes")


class PlaneDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Plane
    success_url = reverse_lazy("management:planes")


class FlightListView(LoginRequiredMixin, generic.ListView):
    model = Flight
    paginate_by = 5


class FlightDetailView(LoginRequiredMixin, generic.DetailView):
    model = Flight


class FlightCreateView(LoginRequiredMixin, generic.CreateView):
    model = Flight
    form_class = FlightForm
    success_url = reverse_lazy("management:flights")


class FlightUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Flight
    form_class = FlightForm
    success_url = reverse_lazy("management:flights")


class FlightDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Flight
    success_url = reverse_lazy("management:flights")


class StaffListView(LoginRequiredMixin, generic.ListView):
    model = Staff
    paginate_by = 5


class StaffDetailView(LoginRequiredMixin, generic.DetailView):
    model = Staff


class StaffCreateView(LoginRequiredMixin, generic.CreateView):
    model = Staff
    form_class = StaffForm
    success_url = reverse_lazy("management:staff")


class StaffUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Staff
    form_class = StaffForm
    success_url = reverse_lazy("management:staff")


class StaffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Staff
    success_url = reverse_lazy("management:staff")
