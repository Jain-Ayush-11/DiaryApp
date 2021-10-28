from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from DiaryApp.settings import STATIC_URL
                              
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.index, name='index'),
    path('Notes/<int:pk>/', views.viewNote, name='notes'),
    path('addnote/', views.add_note, name='addnote'),
    path('task/<int:pk>', views.task, name='task'),
    path('bookmarks/', views.bookmark, name='bookmarks'),
    path('isBookmark/<int:pk>', views.isBookmark, name='isBookmark'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('Notes/Collections/<int:pk>', views.viewCollection, name='viewCollection'),
]

urlpatterns += static(STATIC_URL, document_root = STATIC_URL)
# urlpatterns = format_suffix_patterns(urlpatterns)