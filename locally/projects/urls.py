from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('donations/', views.DonationList.as_view()),
    path('donations/<int:pk>/', views.DonationDetail.as_view()),
    # path('locations/', views.get_all_locations())

    ]
    
urlpatterns = format_suffix_patterns(urlpatterns)
