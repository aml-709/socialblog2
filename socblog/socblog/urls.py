from django.urls import path, include
from django.contrib import admin

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include('socblog.usersup.urls')), 
    path('', include('django.contrib.auth.urls'))
]