from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order,OrderItem

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     fields = ['id', 'order', 'product', 'quantity', 'price',]
#     extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_modified', 'is_paid']

    # inlines = [
    #     OrderItemInline,
    # ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', 'datetime_created']
