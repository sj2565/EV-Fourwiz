from django.urls import path, re_path
from graph import views

#graph App url파일
app_name='graph'    #연동

urlpatterns =[
    path('',views.DataLV.as_view, name='index'),
    path('data/', views.DataLV.as_view(), name='data_list'),
    re_path(r'^data/(?P<pk>[-\w]+)/$', views.DataDV.as_view(), name='data_detail'),


]