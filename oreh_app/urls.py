from django.urls import path

from oreh_app import views

urlpatterns = [
    path(r'achievements/(?P<achievement_id>\d+)/', views.IndexView.as_view(), name = 'achievements')
]
