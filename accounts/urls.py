from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('accounts/signup/', views.registro, name='signup'),
    path('plataforma/', views.index, name='index_logado'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change_done/', views.password_change_done, name='password_change_done'),
    path('dashboard/', views.dashboard, name='painel'),  
    path('conta/', views.conta, name='conta'), 


    ]
