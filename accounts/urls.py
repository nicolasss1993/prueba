from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import *

urlpatterns = [
    # Auth built-in
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),

    # Registro y perfil
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_detail, name='profile_detail'),
    path('profile/edit/', profile_edit, name='profile_edit'),
]