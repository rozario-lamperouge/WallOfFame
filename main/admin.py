from django.contrib import admin
from main.models import College, Student, Review

# Register your models here.
admin.site.register(Student)
admin.site.register(College)
admin.site.register(Review)