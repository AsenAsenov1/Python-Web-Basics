from django.urls import path
from urls_views_project.departments import views

urlpatterns = [
    path('', views.index)
]
