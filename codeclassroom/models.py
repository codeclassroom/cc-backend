'''For signup api endpoint we are expecting json response 
   {'user':'Gagansingh','password':#########,'choice':'Student/Professor'}
   depending on choice we will create their student or prof model
'''
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    ProfilePic = models.ImageField(upload_to='StudentProfilePic', blank=True)
    College_Name = models.CharField(max_length=200, blank=True)
    Course = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Professor(models.Model):
    '''I'm assuming a professor can create multiple classrooms and each classroom can have 
    multiple classroom. if a classroom is deleted, all of the assignments of that class will
    delete automatically.
    '''
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    ProfilePic = models.ImageField(upload_to='ProfessorProfilePic', blank=True)
    College_Name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    professor = models.ForeignKey(to=Professor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    students = models.ManyToManyField(to=Student, blank=True)
    #because a student can join multiple classroom and each classroom can have multiple 
    #students.For more info, refer to official docs

    class Meta:
        verbose_name = 'ClassRoom'
        verbose_name_plural = 'ClassRooms'

    def __str__(self):
        return self.title


class Assignment(models.Model):
    classroom = models.ForeignKey(to=ClassRoom, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    assignment = models.ForeignKey(to=Assignment, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    sample_input = models.TextField(blank=True)
    sample_output = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Response(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    answer = models.CharField(max_length=40000, blank=False)
    remark = models.CharField(max_length=500, blank=True) # this field may be filled by prof as remark

### this project is built by "codeclassroom" organisation and all rights are thereby
#reserved.Please ask before copying this code or project
# happy coding!!!
