from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dayfinder/', include('dayfinder.urls')),
    path('admin/', admin.site.urls),
]