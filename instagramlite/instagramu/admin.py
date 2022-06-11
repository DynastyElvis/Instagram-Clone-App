from django.contrib import admin

# Register your models here.
from .models import Image,Profile,Comment,Follow

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields=('name','image','caption','profile','likes')
    list_display = ('name','image','caption','posted')
    list_filter = ('posted',)
    search_fields = ('name',)
    ordering = ('posted',)
# Register your models here.
