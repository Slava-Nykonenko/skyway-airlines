from datetime import (
    date,
    datetime,
    timedelta
)

from django.contrib.auth import get_user_model
from django.test import TestCase

from management.forms import (
    StaffForm,
    StaffSearchForm,
    AirportForm,
    PlaneForm,
    FlightForm,
    FlightSearchForm,
    AirportSearchForm,
    PlaneSearchForm
)
from management.models import (
    Plane,
    Airport
)


class FormsTest(TestCase):
    def setUp(self):
        self.admin = get_user_model().objects.create(
            username="test.admin",
            password="kljjfJJGJ123",
            email="mjbfjbf@bcb.com",
            first_name="Admin",
            last_name="Admin",
            position="pilot"
        )
        self.client.force_login(self.admin)

    def test_staff_create(self):
        airport = Airport.objects.create(
            iata="DUB",
            name="Dublin International Airport",
            city="Dublin",
            country="Ireland",
            timezone="Europe/Dublin",
            latitude="53.4213",
            longitude="-6.2701"
        )
        plane = Plane.objects.create(
            model="Beechcraft Bonanza",
            registration="S899J",
            capacity=6,
            last_maintenance=date.today(),
            hours_to_maintenance=50,
            total_hours=100
        )
        form_data = {
            "username": "pilot",
            "password1": "JHGHkhjghg515",
            "password2": "JHGHkhjghg515",
            "email": "email@example.com",
            "phone_number": "0855551212",
            "first_name": "First",
            "last_name": "Last",
            "licence_number": "JUL12345",
            "position": "pilot",
            "total_hours": 100,
            "allowed_planes": [plane.id],
            "allowed_airports": [airport.id],
        }
        form = StaffForm(form_data)
        self.assertTrue(form.is_valid())

    def test_airport_create(self):
        form_data = {
            "iata": "DUB",
            "name": "Dublin International Airport",
            "city": "Dublin",
            "country": "Ireland",
            "timezone": "Europe/Dublin",
            "latitude": "53.4213",
            "longitude": "-6.2701"
        }
        form = AirportForm(form_data)
        self.assertTrue(form.is_valid())

    def test_plane_create(self):
        form_data = {
            "model": "Beechcraft Bonanza",
            "registration": "S899J",
            "capacity": 6,
            "last_maintenance": date.today().strftime("%d/%m/%Y"),
            "hours_to_maintenance": 50,
            "total_hours": 100
        }
        form = PlaneForm(form_data)
        self.assertTrue(form.is_valid())

    def test_flight_create(self):
        plane = Plane.objects.create(
            model="Beechcraft Bonanza",
            registration="S899J",
            capacity=6,
            last_maintenance=date.today(),
            hours_to_maintenance=50,
            total_hours=100
        )
        airport = Airport.objects.create(
            iata="DUB",
            name="Dublin International Airport",
            city="Dublin",
            country="Ireland",
            timezone="Europe/Dublin",
            latitude="53.4213",
            longitude="-6.2701"
        )
        staff_member = get_user_model().objects.create_user(
            username="test",
            first_name="Test",
            last_name="Test",
            password="kljjfJJGJ123",
            email="email@example.com",
            licence_number="JUL12345",
            position="pilot",
            phone_number="0855551212",
        )
        staff_member.allowed_airports.set([airport])
        staff_member.allowed_planes.set([plane])

        form_data = {
            "flight_number": "TST111",
            "plane": plane.id,
            "departure": airport.id,
            "destination": airport.id,
            "takeoff": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "landing": (
                datetime.now() + timedelta(hours=2)
            ).strftime("%d/%m/%Y %H:%M"),
            "staff": [staff_member.id],
            "status": "scheduled",
        }
        form = FlightForm(form_data)
        if not self.assertTrue(form.is_valid()):
            print(form.errors)

    def test_airport_search(self):
        form_data = {
            "name": "Dublin",
        }
        form = AirportSearchForm(form_data)
        self.assertTrue(form.is_valid)

    def test_plane_search(self):
        form_data = {
            "model": "Beechcraft Bonanza",
        }
        form = PlaneSearchForm(form_data)
        self.assertTrue(form.is_valid())

    def test_flight_search(self):
        form_data = {
            "flight_number": "test",
        }
        form = FlightSearchForm(form_data)
        self.assertTrue(form.is_valid())

    def test_staff_search(self):
        form_data = {
            "last_name": "staff_search",
        }
        form = StaffSearchForm(form_data)
        self.assertTrue(form.is_valid())
