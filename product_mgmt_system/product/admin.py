from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)

admin.site.register(Product, ProductAdmin)
