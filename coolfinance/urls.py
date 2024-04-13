from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('create_ativo/',views.create_ativo, name='create_ativo' ),
    path('read_ativo/',views.read_ativo, name='read_ativo' ),
    path('update_ativo/<int:ativo_id>/', views.update_ativo, name='update_ativo'),
    path('delete_activo/<int:ativo_id>/', views.delete_activo, name='delete_activo'),

    path('create_passivo/',views.create_passivo, name='create_passivo' ),
    path('read_passivo/',views.read_passivo, name='read_passivo' ),
    path('update_passivo/<int:passivo_id>/',views.update_passivo, name='update_passivo' ),
    path('delete_passivo/<int:passivo_id>/', views.delete_passivo, name='delete_passivo'),

    path('balance/',views.balance, name='balance' ),
    path('',views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)