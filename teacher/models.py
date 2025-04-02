from django.db import models

# Create Teachers Table
class Teacher(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    teacher_id = models.CharField(max_length=50, unique=True)  # Fixed typo: 'unqiue' to 'unique'
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    enlistment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"
    

class Course(models.Model):
    course_id = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=50)
    credits = models.CharField(max_length=100)  # Consider using PositiveIntegerField for credits

    def __str__(self):
        return f"{self.course_id} - {self.course_name}"
    

class Department(models.Model):
    department_id = models.CharField(max_length=10, unique=True)
    department_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'course')

    def __str__(self):
        return f"{self.teacher.first_name} department of {self.department_name} ({self.department_id})"