from django.urls import path, re_path

from oreh_app import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('graduates/', views.GraduatesView.as_view()),
    path('courses/', views.CoursesView.as_view()),
    re_path(r'^courses/(?P<course_id>\d+)/$', views.CourseView.as_view(), name='course'),
]
