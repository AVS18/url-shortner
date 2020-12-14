from django.contrib import admin
from .models import User,SiteAnnouncement,Url

# Register your models here.
class SiteRef(admin.ModelAdmin):
    list_display = ['message']
    list_filter = ['link_exist']

class UrlRef(admin.ModelAdmin):
    list_display = ['shorter_name','original_link','created_by','visitor']
    list_filter = ['created_by','created_at']

admin.site.register(User)
admin.site.register(SiteAnnouncement,SiteRef)
admin.site.register(Url,UrlRef)