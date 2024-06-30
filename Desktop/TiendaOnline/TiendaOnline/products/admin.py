from django.contrib import admin
from .models import Product 


class ProductAdmin(admin.ModelAdmin):#esto es para mostrar en el formulario de admin lo que quiero ver
    fields = ("title", "description", "price","image")
    list_display = ("__str__", "slug", "created_at")
    


admin.site.register(Product, ProductAdmin)