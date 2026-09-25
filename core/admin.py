from django.contrib import admin
from .models import Student, Course


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'phone', 'department')
    search_fields = ('name', 'email', 'department')
    list_filter = ('age', 'department')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration')
    search_fields = ('course_name',)
    list_filter = ('duration',)