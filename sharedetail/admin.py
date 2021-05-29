from django.contrib import admin
from .models import ShareBrought, ShareSold

# Register your models here.


@admin.register(ShareBrought)
class ShareBroughtAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(ShareSold)