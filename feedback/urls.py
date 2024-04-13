from django.urls import path
from . import views
urlpatterns = [
    path('plataforma/feedback/', views.feedback, name='feedback'),
    ]
