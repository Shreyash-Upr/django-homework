from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Teacher, Course, Department
from .forms import TeacherForm, CourseForm, DepartmentForm

# TEACHER VIEWS

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher/teacher_list.html'
    context_object_name = 'teachers'
    ordering = ['last_name', 'first_name']

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher/teacher_detail.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.filter(teacher=self.object)
        return context

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm  # Use form_class instead of model_form
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teacher-list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm  # Use form_class instead of model_form
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teacher-list')

class TeacherDeleteView(DeleteView):  # Adding TeacherDeleteView
    model = Teacher
    template_name = 'teacher/teacher_confirm_delete.html'  # Make sure this template exists
    success_url = reverse_lazy('teacher-list')

# DASHBOARD

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm  # Use form_class instead of model_form
    template_name = 'teacher/course_form.html'  # Ensure this template exists
    success_url = reverse_lazy('course_list')

class CourseListView(ListView):
    model = Course
    template_name = 'teacher/course_list.html'  # Ensure this template exists
    context_object_name = 'courses'
    ordering = ['name']  # Adjust ordering as needed

def dashboard(request):
    context = {
        "teacher_count": Teacher.objects.count(),
        "course_count": Course.objects.count(),
        "department_count": Department.objects.count(),
        "teachers": Teacher.objects.all()[:5],
        "enlistment_date": Teacher.objects.order_by('-enlistment_date')[:5],
    }
    return render(request, 'dashboard.html', context)

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # You'll need to create a 'home.html' template
