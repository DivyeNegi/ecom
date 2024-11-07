from django.contrib import admin

# Register your models here.
from .models import Profile, Order, CartItem



class CartItemAdmin(admin.StackedInline):
    model = CartItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [CartItemAdmin]

admin.site.register(Profile)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem)
