from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('async-view/', views.async_view),
    path('sync-view/', views.sync_view),
]
