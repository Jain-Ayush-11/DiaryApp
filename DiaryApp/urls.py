from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('diary.urls')),
    path('api/', include('diary.api.urls')),
    path('admin/', admin.site.urls),
]
