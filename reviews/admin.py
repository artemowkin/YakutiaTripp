from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'text', 'moderated', 'pub_date']
    list_filter = ['pub_date', 'moderated']
    search_fields = ['name', 'text']
