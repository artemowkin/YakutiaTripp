from django.contrib import admin

from .models import Tour, TourDay


class TourDayInline(admin.TabularInline):
    model = TourDay


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourDayInline]
    list_display = ['title', 'price', 'city_from', 'city_to', 'views']
