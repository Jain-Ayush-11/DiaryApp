from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="getRoutes"),
    path('Notes/', views.getNotes, name="getNotes"),
    path('Notes/<int:pk>', views.getNote, name="getNotes"),
    path('create-note/', views.createNote, name="create-note"),
    path('update-note/<int:pk>', views.updateNote, name="update-note"),
]