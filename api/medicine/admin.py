from django.contrib import admin

from .models import (
    Generic,
    Manufacturer,
    Medicine
)



admin.site.register(Generic)
admin.site.register(Manufacturer)
admin.site.register(Medicine)
