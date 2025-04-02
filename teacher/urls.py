from django.urls import path
from .import views

urlpatterns=[
    #FOR TEACHER URLS
    path("teachers/", views.TeacherListView.as_view(), name="teacher_list"),
    path("teachers/add/", views.TeacherCreateView.as_view(), name = "teacher_create"),
    path("teachers/<int:pk>/", views.TeacherDetailView.as_view(), name = "teacher_detail"),
    path("teachers/<pk>/edit/", views.TeacherUpdateView.as_view(), name = "teacher_edit"),
    path("teachers/<pk>/delete/", views.TeacherDeleteView.as_view(), name = "teacher_delete"),

    #FOR COURSE URLS
    path("courses/", views.CourseListView.as_view(), name="course_list"),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/<pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('courses/<pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
    path('courses/<pk>/enroll/', views.CourseEnrollView.as_view(), name='course_enroll'),

    #FOR DEPARTMENT URLS
    path("departments/", views.DepartmentListView.as_view(), name="department_list"),
    path('departments/add/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/<pk>/edit/', views.DepartmentUpdateView.as_view(), name='department_edit'),
    path('departments/<pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
    path('departments/<pk>/enroll/', views.DepartmentEnrollView.as_view(), name='department_enroll'),
]