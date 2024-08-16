from django.contrib import admin
from .models import MainMenu
from .models import Service
from .models import Booking
from .models import Profile
from .models import Product


# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    list_display = ('service', 'customer_name', 'customer_email', 'booking_date', 'booking_time', 'user')
    list_filter = ('booking_date', 'service', 'user')
    search_fields = ('customer_name', 'customer_email')
    ordering = ('-booking_date',)

    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        queryset.update(completed=True)

    mark_as_completed.short_description = "Mark selected bookings as completed"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'birth_date')
    search_fields = ('user__username', 'phone', 'email')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'price', 'duration')
    list_filter = ('tier',)
    search_fields = ('name',)
    ordering = ('name',)


class MainMenuAdmin(admin.ModelAdmin):
    list_display = ('item', 'link')
    search_fields = ('item', 'link')


admin.site.register(MainMenu, MainMenuAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Product)
