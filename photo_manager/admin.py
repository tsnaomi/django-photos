from django.contrib import admin
from photo_manager.models import Album, Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('creator', 'image', 'caption', 'published_date',
                    'modified_date')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('creator', 'title', 'description', 'published_date',
                    'modified_date', 'public_album')

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Album, AlbumAdmin)
