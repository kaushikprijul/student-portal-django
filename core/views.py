from django.shortcuts import render
from .models import Student, Course


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})


def about(request):
    students = Student.objects.all()
    return render(request, 'about.html', {'students': students})


def contact(request):
    return render(request, 'contact.html')