from django.urls import path, re_path

from oreh_app import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('residents/', views.ResidentsView.as_view()),
    path('current_project/', views.CurrentProjectsView.as_view()),
    re_path(r'projects/(?P<project_id>\d+)/', views.ProjectView.as_view(), name="project"),
]
