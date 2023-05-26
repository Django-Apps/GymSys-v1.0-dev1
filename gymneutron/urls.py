from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('instructor/', include('instructor.urls')),
    path('client/', include('client.urls')),
    path('training/', include('training.urls')),
    path('settings/', include('settings.urls'))
]
