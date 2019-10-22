from django.contrib import admin

from . models import Question, Assignment, ClassRoom, Student, Professor

admin.site.register(ClassRoom)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Professor)
