from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from management.models import (
    Airport,
    Staff,
    Plane,
    Flight
)


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'


def validate_licence_number(
        licence_number,
):
    if len(licence_number) != 8:
        raise ValidationError("Licence number should consist of 8 characters")
    elif not licence_number[:3].isupper() or not licence_number[:3].isalpha():
        raise ValidationError("First 3 characters should be uppercase letters")
    elif not licence_number[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")

    return licence_number


class StaffForm(forms.ModelForm):
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
            "phone_number",
            "licence_number",
            "position",
            "total_hours",
            "allowed_planes",
            "allowed_airports"
        ]

    def clean_licence_number(self):
        licence_number = self.cleaned_data.get("licence_number")
        return validate_licence_number(licence_number)


class StaffCreateForm(UserCreationForm, StaffForm):
    class Meta(StaffForm.Meta):
        fields = StaffForm.Meta.fields + ["password1", "password2"]


class StaffUpdateForm(UserChangeForm, StaffForm):
    password = None

    class Meta(StaffForm.Meta):
        fields = StaffForm.Meta.fields


class PlaneForm(forms.ModelForm):
    class Meta:
        model = Plane
        fields = '__all__'
        widgets = {
            "last_maintenance": AdminDateWidget(
                    attrs={"type": "date"},
            )
        }


def validate_flight(data: dict):
    for staff_member in data.get("staff"):
        if not data.get("plane") in staff_member.allowed_planes.all():
            raise ValidationError(f"{staff_member} cannot fly on {data.get('plane')}")
        if not data.get("departure") in staff_member.allowed_airports.all():
            raise ValidationError(f"{staff_member} cannot fly from {data.get('departure')}")
        if not data.get("destination") in staff_member.allowed_airports.all():
            raise ValidationError(f"{staff_member} cannot fly to {data.get('destination')}")
    takeoff = data.get("takeoff")
    landing = data.get("landing")
    if takeoff and landing and landing <= takeoff:
        raise ValidationError("Landing must be after takeoff.")
    return data


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

    def clean(self):
        cleaned_data = super().clean()
        validate_flight(cleaned_data)
        return cleaned_data



class AirportSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by airport name"}
        ),
        required=False,
        label="",
    )


class PlaneSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by plane model"}
        ),
        required=False,
        label="",
    )


class FlightSearchForm(forms.Form):
    flight_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by flight number"}
        ),
        required=False,
        label="",
    )


class StaffSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={"placeholder": "Search by last name"}
        ),
        required=False,
        label="",
    )
