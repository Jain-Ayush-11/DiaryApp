from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
                              
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('addnote/', views.add_note, name='addnote'),
    path('bookmarks/', views.bookmark, name='bookmarks'),
    path('isBookmark/<int:pk>', views.isBookmark, name='isBookmark'),
    path('unBookmark/<int:pk>', views.unBookmark, name='unBookmark'),
    path('Notes/<int:pk>/', views.notes, name='notes'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
]