from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.
class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)    #Album을 보여줄 때 Photo 정보도 같이 보여줌
    list_display = ('id', 'name')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album' ,'title' )
