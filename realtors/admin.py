from django.contrib import admin
from .models import Realtor

# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','is_mvp', 'phone', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    list_editable = ('is_mvp',)
    list_filter = ('name',)


admin.site.register(Realtor, RealtorAdmin)
