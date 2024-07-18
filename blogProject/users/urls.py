
from django.urls import path,include
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('signup/', views.signup, name='signup'),
   path('', views.userlogin, name='login'),
   path('userlogout/', views.userlogout, name='logout'),
   path('profile/',views.userprofile,name='profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='users/passreset.html'), name='password_reset'),
   path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='users/passresetdone.html'), name='password_reset_done'),
   path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/passresetconfirm.html'), name='password_reset_confirm'),
   path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/passresetcomplete.html'), name='password_reset_complete'),




    # Add other URLs for user-related views as needed
]

