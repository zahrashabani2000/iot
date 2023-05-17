from django.urls import path

from data import views


urlpatterns = [
    path('', views.ScanView.as_view())
]