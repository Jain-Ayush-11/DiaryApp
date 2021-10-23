from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('Notes/', views.add_note, name='addnote'),
    path('Notes/<int:pk>/', views.notes, name='notes'),
]