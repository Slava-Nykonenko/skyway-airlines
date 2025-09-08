from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm

from management.models import Airport, Staff, Plane, Flight


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'


class StaffForm(UserCreationForm):
    allowed_airports = forms.ModelMultipleChoiceField(
        queryset=Airport.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    allowed_planes = forms.ModelMultipleChoiceField(
        queryset=Plane.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Staff
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "licence_number",
            "position",
            "total_hours",
            "allowed_planes",
            "allowed_airports"
        ]


class PlaneForm(forms.ModelForm):
    class Meta:
        model = Plane
        fields = '__all__'
        widgets = {
            "last_maintenance": AdminDateWidget(
                    attrs={"type": "date"},
            )
        }


class FlightForm(forms.ModelForm):
    staff = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Flight
        fields = [
            "flight_number",
            "plane",
            "departure",
            "destination",
            "takeoff",
            "landing",
            "staff",
            "status"
        ]
        widgets = {
            "takeoff": forms.DateTimeInput(
                format="%d/%m/%Y %H:%M",
                attrs={"type": "datetime-local"}
            ),
            "landing": forms.DateTimeInput(
                format="%d/%m/%Y %H:%M",
                attrs={"type": "datetime-local"}
            ),
        }
