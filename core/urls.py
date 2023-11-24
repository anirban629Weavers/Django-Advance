from django.contrib import admin
from django.urls import path
from home.views import home,contact,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="Home base"),
    path('about/', about,name="about"),
    path('contact/', contact,name="contact"),
]
