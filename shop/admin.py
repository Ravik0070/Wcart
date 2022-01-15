from django.contrib import admin
from shop.models import Product,Category

class CatergoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields={'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','created','updated']
    list_filter = ['available','created','updated']
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CatergoryAdmin)
admin.site.register(Product,ProductAdmin)