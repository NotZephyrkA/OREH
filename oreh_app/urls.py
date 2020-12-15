from django.urls import path

from oreh_app import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('graduates/', views.GraduatesView.as_view()),
]
