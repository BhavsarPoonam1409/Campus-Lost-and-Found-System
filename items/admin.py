from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        'item_name',
        'report_type',
        'category',
        'location',
        'status',
        'reported_by',
        'created_at',
    )

    list_filter = (
        'report_type',
        'category',
        'status',
    )

    search_fields = (
        'item_name',
        'category',
        'location',
        'reported_by__username',
    )

