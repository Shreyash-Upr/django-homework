from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),
    
    # Root URL redirects to the teacher list
    path('', include('teacher.urls')),

    # Include teacher URLs
    path('teachers/', include('teacher.urls')),
]
