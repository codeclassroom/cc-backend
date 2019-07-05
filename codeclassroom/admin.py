from django.contrib import admin

# Register your models here.
from . models import Questions, Assignments, ClassRoom, Student, Professor

admin.site.register(ClassRoom)
admin.site.register(Assignments)
admin.site.register(Questions)
admin.site.register(Student)
admin.site.register(Professor)