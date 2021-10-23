from django.urls import path

from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('addnote/', views.add_note, name='addnote'),
    path('Notes/<int:pk>/', views.notes, name='notes'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]