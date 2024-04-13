
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('coolfinance.urls')),
    path('',include('accounts.urls')),
    path('',include('feedback.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
