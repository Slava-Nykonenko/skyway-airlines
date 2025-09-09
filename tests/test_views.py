from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.test import (
    TestCase,
    Client
)
from django.urls import reverse

from management.models import (
    Plane,
    Airport
)


class ViewsUnauthorizedTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_airport_list(self) -> None:
        url = reverse("management:airports")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_airport_create(self) -> None:
        url = reverse("management:airport-create")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_plane_list(self) -> None:
        url = reverse("management:planes")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_plane_create(self) -> None:
        url = reverse("management:plane-create")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_staff_list(self) -> None:
        url = reverse("management:staff")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_staff_create(self) -> None:
        url = reverse("management:staff-create")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_flight_list(self) -> None:
        url = reverse("management:flights")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

    def test_flight_create(self) -> None:
        url = reverse("management:flight-create")
        res = self.client.get(url)
        self.assertNotEqual(res.status_code, 200)

class ViewsAuthorizedTest(TestCase):
    def setUp(self):
        self.admin = get_user_model().objects.create(
            username="tests.admin",
            password="kljjfJJGJ123",
            email="mjbfjbf@bcb.com",
            first_name="Admin",
            last_name="Admin",
            position="pilot"
        )
        self.client.force_login(self.admin)

    def test_airport_list(self) -> None:
        url = reverse("management:airports")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_airport_create(self) -> None:
        url = reverse("management:airport-create")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_plane_list(self) -> None:
        url = reverse("management:planes")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_plane_create(self) -> None:
        url = reverse("management:plane-create")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_staff_list(self) -> None:
        url = reverse("management:staff")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_staff_create(self) -> None:
        url = reverse("management:staff-create")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_flight_list(self) -> None:
        url = reverse("management:flights")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_flight_create(self) -> None:
        url = reverse("management:flight-create")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)


class StaffViewTests(TestCase):
    def setUp(self):
        self.admin = get_user_model().objects.create_user(
            username="tests.admin",
            password="kljjfJJGJ123",
            email="mjbfjbf@bcb.com",
            first_name="Admin",
            last_name="Admin",
            position="pilot"
        )
        self.client.force_login(self.admin)
        self.plane = Plane.objects.create(
            model="Beechcraft Bonanza",
            registration="S899J",
            capacity=6,
            last_maintenance=date.today(),
            hours_to_maintenance=50,
            total_hours=100
        )
        self.airport = Airport.objects.create(
            iata="DUB",
            name="Dublin International Airport",
            city="Dublin",
            country="Ireland",
            timezone="Europe/Dublin",
            latitude="53.4213",
            longitude="-6.2701"
        )

    def test_toggle_assign_to_plane(self):
        url = reverse(
            "management:toggle-assign-to-plane",
            args=[self.plane.pk]
        )
        self.client.get(url)
        self.assertIn(self.plane, self.admin.allowed_planes.all())

    def test_toggle_assign_to_airport(self):
        url = reverse(
            "management:toggle-assign-to-airport",
            args=[self.airport.pk]
        )
        self.client.get(url)
        self.assertIn(self.airport, self.admin.allowed_airports.all())

    def test_change_password(self):
        url = reverse(
            "management:password",
            args=[self.admin.id]
        )
        response = self.client.post(
            url,
            {
                "old_password": "kljjfJJGJ123",
                "new_password1": "NewSecurePassword456",
                "new_password2": "NewSecurePassword456"
            }
        )
        self.admin.refresh_from_db()
        self.assertTrue(
            self.admin.check_password(
                "NewSecurePassword456"
            )
        )
        self.assertRedirects(
            response,
            reverse(
                "management:staff-detail",
                args=[self.admin.id]
            )
        )
