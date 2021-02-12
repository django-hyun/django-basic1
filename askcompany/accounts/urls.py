from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('login/', LoginView.as_view(template_name='accounts/login_form.html'), name='login'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('signup/', views.signup, name='signup'),
    path ('logout/', LogoutView.as_view (), name='logout'),

]

