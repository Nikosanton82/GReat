from django.contrib import admin
from . models import Category, MenuItem
from django.utils.text import slugify
import uuid

admin.site.register(Category)

# class MenuItemAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if not obj.pk:
#             obj.slug = slugify(obj.name)
#             while MenuItem.objects.filter(slug=obj.slug).exists():
#                 obj.slug = f'{obj.slug}-{str(uuid.uuid4())[:8]}'
#         obj.save()

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'ingredients', 'sauce')
    search_fields = ('name', 'category__name', 'ingredients', 'sauce')
    list_filter = ('category',)


admin.site.register(MenuItem, MenuItemAdmin)