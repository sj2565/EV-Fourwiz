from django.urls import path, re_path, include
from blog import views
from d3_korea_map.map import show_korea_map

app_name = 'blog'
urlpatterns = [

    # Example: /blog/
    path('', views.MapV.as_view(), name='map_all'),

    # Example: /blog/
    path('', views.MapLV.as_view(), name='index'),

    # Example: /blog/map/
    path('map/', views.MapLV.as_view(), name='map_list'),

    path('', show_korea_map, name='KoreaMap'),

    # Example: /blog/map/django-example
    re_path(r'^map/(?P<slug>[-\w]+)/$', views.MapDV.as_view(), name='map_detail'),

]