from django.contrib import admin
from .models import Academic,Skill,User,Cv,Profile,Referee,Experience,Project

# Register your models here.
model_list = [User, Skill, Cv,Academic,Profile,Referee,Experience,Project]
admin.site.register(model_list)
