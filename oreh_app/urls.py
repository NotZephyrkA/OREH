from django.urls import path

from oreh_app import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('residents/', views.ResidentsView.as_view()),
    path('current_project/', views.CurrentProjectsView.as_view()),
]
