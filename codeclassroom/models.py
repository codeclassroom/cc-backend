from django.db import models
from django.contrib.auth.models import User

'''From signup api endpoint we are expecting json response be like
   {'user':'Gagansingh','password':#########,'choice':'Student/Professor'}
   depending on choice we will create their student or prof model'''


class Student(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=100,blank=True)
	ProfilePic=models.ImageField(upload_to='StudentProfilePic',blank=True)
	College_Name=models.CharField(max_length=200,blank=True)
	Course=models.CharField(max_length=50,blank=True)

class Professor(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=100,blank=True)
	ProfilePic=models.ImageField(upload_to='ProfessorProfilePic',blank=True)
	College_Name=models.CharField(max_length=200,blank=True)

'''I'm assuming a professor can create multiple classrooms and each classroom can have 
multiple classroom. if a classroom is deleted, all of the assignments of that class will
delete automatically'''

class ClassRoom(models.Model):
   professor=models.ForeignKey(Professor,on_delete=models.CASCADE)
   title=models.CharField(max_length=200,blank=False)
   Picture=models.ImageField(upload_to='ClassMedia',blank=False)
   student=models.ManyToManyField(Student,blank=True)
   #because a student can join multiple classroom and each classroom can have multiple 
   #students.For more info, refer to official docs


class Assignments(models.Model):
   classroom=models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
   title=models.CharField(max_length=200,blank=False)

class Questions(models.Model):
	assignment=models.ForeignKey(codeclassroom,on_delete=models.CASCADE)
	content=models.CharField(max_length=2000,blank=False)

'''NOW i will be making a reponse model ,i.e., response of a student for a assignment

'''
class Respopnse(models.Model):
	question=models.ForeignKey(Questions,on_delete=models.CASCADE)
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	answer=models.CharField(max_length=40000,blank=False)
	remark=models.CharField(max_length=500,blank=True)#this field may be filled by prof 
	#as remark

### this project is built by "codeclassroom" organisation and all rights are thereby
#reserved.Please ask before copying this code or project
# happy coding!!!

