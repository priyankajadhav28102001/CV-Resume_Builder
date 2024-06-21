from django.db import models
from django.contrib.auth.models import AbstractUser
from distutils.command.upload import upload

# Create your models here.
class User(AbstractUser):
    is_user=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Cv(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
class Skill(models.Model):
    cv = models.ForeignKey(Cv,on_delete=models.CASCADE)
    s_name = models.CharField(max_length=500)
    s_level =models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.s_name
    
class Experience(models.Model):
    cv= models.ForeignKey(Cv,on_delete=models.CASCADE)
    e_office =models.CharField(max_length=500)
    e_position =models.CharField(max_length=500)
    e_responsibilities =models.CharField(max_length=500)
    e_startdate = models.DateField(null=True, blank=True)
    e_enddate = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.e_office
    
class Project(models.Model):
    cv= models.ForeignKey(Cv,on_delete=models.CASCADE)
    p_projectname =models.CharField(max_length=500)
    p_description =models.TextField(max_length=10000, help_text="Enter a brief description of the project")
    p_startdate = models.DateField(null=True, blank=True)
    p_enddate = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.p_name    

      
class Academic(models.Model):
    cv= models.ForeignKey(Cv,on_delete=models.CASCADE)
    a_institution =models.CharField(max_length=500)
    a_year =models.CharField(max_length=500) 
    a_award =models.CharField(max_length=500) 

    def __str__(self) -> str:
        return self.a_institution
    
class Certificate(models.Model):
    cv= models.ForeignKey(Cv,on_delete=models.CASCADE)
    c_certificate =models.CharField(max_length=500)
    c_year =models.CharField(max_length=500) 

    def __str__(self) -> str:
        return self.c_certificate
    

    
class Referee(models.Model):
    cv= models.ForeignKey(Cv,on_delete=models.CASCADE)
    r_name =models.CharField(max_length=500) 
    r_email =models.CharField(max_length=500) 
    r_phone =models.CharField(max_length=500) 

    def __str__(self) -> str:
        return self.r_name    

class Profile(models.Model):
     cv= models.ForeignKey(Cv,on_delete=models.CASCADE)
     fname =models.CharField(max_length=500)
     lname =models.CharField(max_length=500)
     mname =models.CharField(max_length=500)
     gender =models.CharField(max_length=500)
     country =models.CharField(max_length=500)
     region =models.CharField(max_length=500)
     email =models.CharField(max_length=500)
     phone =models.CharField(max_length=500)
     occupation =models.CharField(max_length=500)
     dob =models.DateField(default="None")
     bio =models.TextField()
    

     def __str__(self) -> str:
         return self.fname
     
     def delete(self, *args, **kwargs):
         self.avator.delete()
         super().delete(*args,**kwargs)

         






