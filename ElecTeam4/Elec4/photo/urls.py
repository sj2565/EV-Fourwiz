# ch09에서 신규 생성된 파일
from django.urls import path
from photo import views

app_name = 'photo'

urlpatterns = [
    # Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # Example: /photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    #10/12
    path('album/thumb/<int:pk>', views.AlbumTH.as_view(), name='album_thumb'),

    # Example: /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # Example: /photo/photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),


####ch12에서 추가-album/
    # Example: /photo/photo/add/
    path('album/add/', views.AlbumPhotoCreateView.as_view(), name='album_add'),

    # Example: /photo/album/change/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),

    # Example: /photo/album/99/update/
    path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'),

    # Example: /photo/album/99/delete/
    path('album/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),

####ch12에서 추가-photo/
    # Example: /photo/photo/add/
    path('photo/add/', views.PhotoCreateView.as_view(), name='photo_add'),

    # Example: /photo/photo/change/
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),

    # Example: /photo/photo/99/update/
    path('photo/<int:pk>/update/', views.PhotoUpdateView.as_view(), name='photo_update'),

    # Example: /photo/photo/99/delete/
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
]
