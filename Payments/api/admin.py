from django.contrib import admin

from Payments.settings import VALUE_DISPLAY
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('stripe_price_id', 'name', 'price', 'currency')
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = VALUE_DISPLAY
