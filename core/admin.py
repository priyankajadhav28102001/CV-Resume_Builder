from django.contrib import admin
from .models import Academic,Skill,User,Cv,Profile,Referee,Experience,Project,Certificate

# Register your models here.
model_list = [User, Skill, Cv,Academic,Profile,Referee,Experience,Project,Certificate]
admin.site.register(model_list)
