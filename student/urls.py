
from django.contrib import admin
from django.urls import path
from student_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home)
]
