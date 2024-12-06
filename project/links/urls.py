from django.urls import path
from . import views

app_name = 'links'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('watch/', views.watch, name='watch'),
  path('watch/<int:categoryId>', views.watch, name='watch'),
]