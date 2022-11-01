from django.contrib import admin

from houses.models import House

# Register your models here.


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):

    list_display = ["name", "price", "address", "pets_allowed"]
    list_filter = ["price", "pets_allowed", "description"]
    search_fields = ["address"]
