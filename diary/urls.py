from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
                              
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('addnote/', views.add_note, name='addnote'),
    path('task/<int:pk>', views.task, name='task'),
    path('bookmarks/', views.bookmark, name='bookmarks'),
    path('isBookmark/<int:pk>', views.isBookmark, name='isBookmark'),
    path('Notes/<int:pk>/', views.notes, name='notes'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]