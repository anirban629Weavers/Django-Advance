from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home.views import home,contact,about
from vege.views import recipes,delete_recipe,update_recipe,login_user,register_user,logout_user

from django.contrib.auth import views as auth_views

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

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="vege/reset_password.html"),
         name="reset_password"),
    path('reset_password_set/', 
         auth_views.PasswordResetDoneView.as_view(template_name="vege/reset_password_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="vege/reset.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="vege/reset_password_complete.html"),
         name="password_reset_complete")

]

urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)