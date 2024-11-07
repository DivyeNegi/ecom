from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class StorageAdmin(admin.StackedInline):
    model = Storage

class ColorAdmin(admin.StackedInline):
    model = Color

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, StorageAdmin, ColorAdmin]


admin.site.register(Product, ProductAdmin)

admin.site.register(Storage)

admin.site.register(Color)

admin.site.register(ProductImage)
