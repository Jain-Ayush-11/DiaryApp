from django.urls import path

from . import views

urlpatterns = [
    path('Notes/', views.NotesList.as_view(), name="getNote"),
    path('Notes/<int:pk>', views.NoteDetails.as_view(), name="getNotes"),
    path('Notes/collections/', views.CollectionList.as_view(), name="collection"),
    path('Notes/create-note/', views.NotesList.as_view(), name="create-note"),
    path('Notes/update-note/<int:pk>', views.NoteDetails.as_view(), name="update-note"),
    path('Notes/delete-note/<int:pk>', views.NoteDetails.as_view(), name="delete-note"),
]