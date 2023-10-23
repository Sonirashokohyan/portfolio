from django.urls import path
from . import views
from .views import download_file

urlpatterns = [
    # path('', views.home, name='members'),
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('download/', download_file, name='download'),
    # path('download_pdf/', views.download_pdf, name='download_pdf'),
    
]


