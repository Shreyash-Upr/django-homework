from django import forms
from .models import Teacher, Course, Department

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'teacher_id', 'date_of_birth','gender', 'email', 'phone_number', 'address']
        widgets={
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'credits']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_id', 'department_name', 'course', 'teacher']