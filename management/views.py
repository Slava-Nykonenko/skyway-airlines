from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.urls import reverse_lazy
from django.views import generic

from management.forms import (
    AirportForm,
    PlaneForm,
    FlightForm,
    AirportSearchForm,
    PlaneSearchForm,
    FlightSearchForm,
    StaffSearchForm,
    StaffCreateForm,
    StaffUpdateForm
)
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

    def get_context_data(
        self, *, object_list=None, **kwargs
    ):
        context = super(AirportListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = AirportSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Airport.objects.all()
        form = AirportSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return queryset


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

    def get_context_data(
        self, *, object_list=None, **kwargs
    ):
        context = super(PlaneListView, self).get_context_data(**kwargs)
        model = self.request.GET.get("model", "")
        context["search_form"] = PlaneSearchForm(
            initial={"model": model}
        )
        return context

    def get_queryset(self):
        queryset = Plane.objects.all()
        form = PlaneSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                model__icontains=form.cleaned_data["model"]
            )
        return queryset


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

    def get_context_data(
        self, *, object_list=None, **kwargs
    ):
        context = super(FlightListView, self).get_context_data(**kwargs)
        flight_number = self.request.GET.get("flight_number", "")
        context["search_form"] = FlightSearchForm(
            initial={"flight_number": flight_number}
        )
        return context

    def get_queryset(self):
        queryset = Flight.objects.all().select_related(
            "departure",
            "destination",
            "plane"
        )
        form = FlightSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                flight_number__icontains=form.cleaned_data[
                    "flight_number"
                ]
            )
        return queryset


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

    def get_context_data(
        self, *, object_list=None, **kwargs
    ):
        context = super(StaffListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name", "")
        context["search_form"] = StaffSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        queryset = Staff.objects.all()
        form = StaffSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            )
        return queryset


class StaffDetailView(LoginRequiredMixin, generic.DetailView):
    model = Staff


class StaffCreateView(LoginRequiredMixin, generic.CreateView):
    model = Staff
    form_class = StaffCreateForm
    success_url = reverse_lazy("management:staff")


class StaffUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Staff
    form_class = StaffUpdateForm
    success_url = reverse_lazy("management:staff")


class StaffDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Staff
    success_url = reverse_lazy("management:staff")


@login_required
def toggle_assign_to_plane(request, pk):
    staff_member = Staff.objects.get(id=request.user.id)
    plane = Plane.objects.get(id=pk)
    if (
        plane in staff_member.allowed_planes.all()
    ):
        staff_member.allowed_planes.remove(plane)
    else:
        staff_member.allowed_planes.add(plane)
    return HttpResponseRedirect(
        reverse_lazy("management:plane-detail", args=[pk])
    )


@login_required
def toggle_assign_to_airport(request, pk):
    staff_member = Staff.objects.get(id=request.user.id)
    airport = Airport.objects.get(id=pk)
    if (
        airport in staff_member.allowed_airports.all()
    ):
        staff_member.allowed_airports.remove(airport)
    else:
        staff_member.allowed_airports.add(airport)
    return HttpResponseRedirect(
        reverse_lazy("management:airport-detail", args=[pk])
    )


@login_required
def change_password(request, pk):
    user = get_object_or_404(Staff, pk=pk)

    if request.method == "POST":
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)  # Keeps user logged in
            messages.success(request, "Password updated successfully.")
            return redirect("management:staff-detail", pk=pk)
    else:
        form = PasswordChangeForm(user=user)

    return render(
        request,
        "management/change_password.html",
        {
            "form": form,
            "staff": user
        }
    )
