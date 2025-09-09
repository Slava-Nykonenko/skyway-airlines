from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Airport,
    Plane,
    Staff,
    Flight
)


@admin.register(Staff)
class StaffAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("licence_number",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                        "licence_number",
                    )
                },
            ),
        )
    )


@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = (
        "capacity",
        "last_maintenance",
        "hours_to_maintenance",
        "total_hours"
    )


admin.site.register(Flight)


class FlightAdmin(admin.ModelAdmin):
    search_fields = ("flight_number",)
    list_filter = (
        "departure",
        "takeoff",
        "destination",
        "landing",
        "status"
    )


admin.site.register(Airport)


class AirportAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = (
        "city",
        "country",
    )
