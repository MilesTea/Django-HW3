from django.contrib import admin
from phones import models

# Register your models here.


@admin.register(models.Phone)
class PhoneAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'image', 'price', 'release_date', 'lte_exists', 'slug']
	prepopulated_fields = {'slug': ('name',)}
