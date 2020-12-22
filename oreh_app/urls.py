from django.urls import path, re_path

from oreh_app import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    re_path(r'achievements/', views.AchievementView.as_view(), name='achievements'),
]
