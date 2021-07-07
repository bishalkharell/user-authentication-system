from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_users.urls')),
    path('', include('django.contrib.auth.urls')),


]
