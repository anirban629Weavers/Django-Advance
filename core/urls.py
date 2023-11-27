from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home,contact,about
from vege.views import recipes,delete_recipe,update_recipe,login_user,register_user,logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="Home base"),
    path('about/', about,name="about"),
    path('contact/', contact,name="contact"),
    path('recipes/', recipes,name="recipes"),
    path('delete-recipe/<id>/', delete_recipe,name="delete-recipes"),
    path('update-recipe/<id>/', update_recipe,name="delete-recipes"),
    path('login/', login_user,name="login"),
    path('logout/', logout_user,name="logout"),
    path('register/', register_user,name="register"),
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)