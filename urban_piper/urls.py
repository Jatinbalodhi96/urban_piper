from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('up_web.urls')),
    path('admin/', admin.site.urls),
]
