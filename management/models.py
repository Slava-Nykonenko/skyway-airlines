from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.urls import reverse


# Create your models here.

class Airport(models.Model):
    iata = models.CharField(
        max_length=20,
        verbose_name="IATA code",
        unique=True)
    name = models.CharField(
        max_length=50,
        verbose_name="Name"
    )
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=5
    )
    longitude = models.DecimalField(
        max_digits=8,
        decimal_places=5,
    )

    class Meta:
        ordering = ["city"]

    def __str__(self):
        return f"{self.iata} - {self.name} ({self.city}, {self.country})"


class Plane(models.Model):
    model = models.CharField(max_length=100)
    registration = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    last_maintenance = models.DateField()
    hours_to_maintenance = models.IntegerField()
    total_hours = models.IntegerField()

    def __str__(self):
        return f"{self.model} ({self.registration})"


class Staff(AbstractUser):
    POSITION_CHOICES = [
        ("pilot", "Pilot"),
        ("co-pilot", "Co-Pilot"),
        ("flight attendant", "Flight Attendant"),
        ("engineer", "Engineer"),
        ("ground crew", "Ground Crew"),
        ("dispatcher", "Dispatcher"),
        ("maintenance tech", "Maintenance Tech"),
        ("cabin crew", "Cabin Crew"),
    ]
    phone_number = models.CharField(
        max_length=13,
        unique=True,
        null=True,
        blank=True
    )
    licence_number = models.CharField(
        max_length=8,
        unique=True,
        null=True,
        blank=True
    )
    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
    )
    total_hours = models.IntegerField(null=True, blank=True)
    allowed_planes = models.ManyToManyField(
        Plane,
        related_name="staff"
    )
    allowed_airports = models.ManyToManyField(
        Airport,
        related_name="staff"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.position})"

    def get_absolute_url(self):
        return reverse(
            "management:staff-detail",
            kwargs={"pk": self.pk}
        )


class Flight(models.Model):
    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("cancelled", "Cancelled"),
        ("delayed", "Delayed"),
    ]
    flight_number = models.CharField(
        max_length=10,
        unique=True
    )
    plane = models.ForeignKey(
        Plane,
        on_delete=models.PROTECT
    )
    departure = models.ForeignKey(
        Airport,
        on_delete=models.PROTECT,
        related_name="departing_flights"
    )
    destination = models.ForeignKey(
        Airport,
        on_delete=models.PROTECT,
        related_name="arriving_flights"
    )
    takeoff = models.DateTimeField()
    landing = models.DateTimeField()
    staff = models.ManyToManyField(
        Staff,
        related_name="flight"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="scheduled"
    )

    def __str__(self):
        return (f"{self.flight_number} "
                f"{self.departure} - {self.destination}")
