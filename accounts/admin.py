from django.contrib import admin

# Register your models here.
from .models import CustomUser

class CustomUsetAdmin(admin.ModelAdmin):
    list_display = ('id','username')
    lst_display_links = ('id','username')
    
admin.site.register(CustomUser, CustomUsetAdmin)

