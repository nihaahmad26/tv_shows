from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('edit', views.edit),
    path('update', views.update),
    path('show', views.show),
    path('delete', views.delete),
]