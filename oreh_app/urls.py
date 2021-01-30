from django.urls import path, re_path

from oreh_app import views

app_name = 'oreh_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path(r'achievements/', views.AchievementView.as_view(), name='achievements'),
    path('residents/', views.ResidentsView.as_view(), name='residents'),
    path('current_project/', views.CurrentProjectsView.as_view(), name='current_project'),
    re_path(r'projects/(?P<project_id>\d+)/', views.ProjectView.as_view(), name="project"),
    re_path(r'residents/(?P<resident_id>\d+)/', views.ResidentView.as_view(), name="resident"),
    path('graduates/', views.GraduatesView.as_view(), name="graduates"),
    path('courses/', views.CoursesView.as_view(), name="courses"),
    re_path(r'^courses/(?P<course_id>\d+)/$', views.CourseView.as_view(), name='course'),
    path('events/', views.EventsView.as_view(), name='events'),
    re_path(r'events/(?P<event_id>\d+)/', views.EventView.as_view(), name="event"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('personal_account/', views.PersonalAccount.as_view(), name='personal_account'),
    re_path(r'graduates/(?P<graduate_id>\d+)/', views.GraduateView.as_view(), name="graduate"),
]
