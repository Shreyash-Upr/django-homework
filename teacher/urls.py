from django.urls import path
from . import views

urlpatterns = [
    path("", views.TeacherListView.as_view(), name="home"),

    # TEACHER URLS
    path("teachers/", views.TeacherListView.as_view(), name="teacher_list"),
    path("teachers/add/", views.TeacherCreateView.as_view(), name="teacher_create"),
    path("teachers/<int:pk>/", views.TeacherDetailView.as_view(), name="teacher_detail"),
    path("teachers/<int:pk>/edit/", views.TeacherUpdateView.as_view(), name="teacher_edit"),
    path("teachers/<int:pk>/delete/", views.TeacherDeleteView.as_view(), name="teacher_delete"),
]
