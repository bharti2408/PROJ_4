
from django.contrib import admin
from django.urls import path
from poll import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", views.Home, name="home"),
    
    path("thank/", views.thank, name="thank"),
    
]
