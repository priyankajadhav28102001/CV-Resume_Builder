import pdfkit
from fileinput import filename
from django.http import HttpResponse, JsonResponse,response
from django.shortcuts import render,redirect,reverse
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from django.template import context
from .models import Skill,Academic,Referee,Profile,User,Skill,Cv,Experience,Project
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from django.urls import path
from pdfkit import from_url


# Create your views here.
def index(request):
    #return HttpResponse('hi')
    return render(request,'core/index.html')

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    return render(request, 'core/login.html')

@login_required
def dashboard(request):
    user_id =request.user.id 

    try:
        cv_id= Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
        cv_id= list(cv_id)
        cv_id= cv_id[0]
        print('Cv ID is',cv_id)
        print('Data type',type(cv_id))
        if isinstance(cv_id,int):
            context ={'status': 'there_is_cv'}
            return render(request, 'core/dashboard.html',context)
    except Exception as e:
        context= {'status': 'no_cv'}
        return render(request, 'core/dashboard.html',context)
    
def createCv(request):
    user_id = request.user.id 
    try:
        cv_id = Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
        cv_id = list(cv_id)
        cv_id = cv_id[0]

        profile_id = Profile.objects.filter(cv_id=cv_id).values_list('id',flat=True)
        profile_id = list(profile_id)
        profile_id = profile_id[0]

        if isinstance(profile_id,int):
            context={'status':'there_is_profile'}
            return render(request, 'core/create_cv.html',context)
    except Exception as e:
        context={'status':'no_profile'}
        return render(request, 'core/create_cv.html',context)
    
def saveSkill(request):
    if request.method == 'POST':
        user_id = request.user.id
        
        cv_id = Cv.objects.filter(user_id=user_id).values_list('id', flat=True)
        cv_id = list(cv_id)
        cv_id = cv_id[0]


        s_name = request.POST.getlist('s_name[]')
        s_level = request.POST.getlist('s_level[]')
        
        if(len(s_name) == 1):
            a = Skill(s_name = s_name[0], s_level=s_level[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y in zip(s_level,s_name):
                a = Skill(s_level=x, s_name=y, cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})
                
 

def saveEducation(request):
    if request.method =='POST':
        name= request.POST.getlist('name[]')
        year =request.POST.getlist('year[]')
        award = request.POST.getlist('award[]')

        user_id =request.user.id 
        cv_id = Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
        cv_id =list(cv_id)
        cv_id =cv_id[0]

        if(len(name)==1):
            a = Academic(a_institution = name[0], a_year=year[0],a_award=award[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(name,year,award):
                a = Academic(a_institution=x, a_year=y, a_award=z,cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})

def saveExperience(request):
    if request.method =='POST':
        name= request.POST.getlist('name[]')
        duration =request.POST.getlist('duration[]')
        position = request.POST.getlist('position[]')

        user_id =request.user.id 
        cv_id = Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
        cv_id =list(cv_id)
        cv_id =cv_id[0]

        if(len(name)==1):
            a = Experience(e_office = name[0], e_duration=duration[0],e_position=position[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(name,duration,position):
                a = Experience(e_office=x, e_duration=y, e_position=z,cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})

def saveProject(request):
    if request.method =='POST':
        name= request.POST.getlist('name[]')
        description =request.POST.getlist('description[]')
        startdate = request.POST.getlist('startdate[]')
        enddate = request.POST.getlist('enddate[]')

        user_id =request.user.id 
        cv_id = Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
        cv_id =list(cv_id)
        cv_id =cv_id[0]

        if(len(name)==1):
            a = Project(p_projectname = name[0], p_description=description[0],p_startdate=startdate[0],p_enddate=enddate[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z,w in zip(name,description,startdate,enddate):
                a = Project(p_projectname=x, p_description=y, p_startdate=z,p_enddate=w,cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})
   
   
                

def saveReferee(request):
    if request.method == 'POST':
        name= request.POST.getlist('name[]')
        phone =request.POST.getlist('phone[]')
        email = request.POST.getlist('email[]')

        user_id =request.user.id 
        cv_id= Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
        cv_id=list(cv_id)
        cv_id=cv_id[0]

        if(len(name)==1):
            a = Referee(r_name = name[0], r_phone=phone[0],r_email=email[0], cv_id=cv_id)
            a.save()
            return JsonResponse({'status':1})
        else:
            for x,y,z in zip(name,phone,email):
                a = Referee(r_name=x, r_phone=y, r_email=z,cv_id=cv_id)
                a.save()
            return JsonResponse({'status':1})
    return JsonResponse({'status':0})

def uploadProfile(request):
    fname = request.POST.get('fname')
    mname  = request.POST.get('mname')
    lname  = request.POST.get('lname')
    email  = request.POST.get('email')
    phone  = request.POST.get('phone')
    gender  = request.POST.get('gender')
    bio  = request.POST.get('bio')
    dob  = request.POST.get('dob')
    occupation  = request.POST.get('occupation')
    country  = request.POST.get('country')
    region  = request.POST.get('region')
    file  = request.FILES.get('file')
    user_id  = request.user.id 

    Cv.objects.create(user_id=user_id)

    cv_id = Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
    cv_id = list(cv_id)
    cv_id = cv_id[0]
    print('Cv Id is',cv_id)

    p=Profile(fname=fname, mname=mname,lname=lname ,email=email ,bio=bio, dob=dob, gender=gender, occupation=occupation, country=country, region=region, avator=file, phone=phone, cv_id=cv_id)
    p.save()
    return JsonResponse({'status':1})

def updateSkill(request):
    id= request.POST.get('id')
    name =request.POST.get('name')
    level =request.POST.get('level')
   
    Skill.objects.filter(id=id).update(s_name=name, s_level=level)
    return JsonResponse({'status':1})

def updateReferee(request):
    id= request.POST.get('id')
    name =request.POST.get('name')
    phone=request.POST.get('phone')
    email =request.POST.get('email')
    
    Referee.objects.filter(id=id).update(r_name=name,r_phone=phone, r_email=email)
    return JsonResponse({'status':1})

def updateAcademic(request):
    id= request.POST.get('id')
    institution =request.POST.get('institution')
    year =request.POST.get('year')
    award =request.POST.get('award')

    Academic.objects.filter(id=id).update(a_institution=institution, a_year=year, a_award=award)
    return JsonResponse({'status':1})

def updateExperience(request):
    id= request.POST.get('id')
    office =request.POST.get('office')
    duration =request.POST.get('duration')
    position =request.POST.get('position')

    Experience.objects.filter(id=id).update(e_office=office, e_duration=duration, e_position=position)
    return JsonResponse({'status':1})

def updateProject(request):
    id= request.POST.get('id')
    projectname= request.POST.get('projectname')
    description =request.POST.get('description')
    startdate = request.POST.get('startdate')
    enddate = request.POST.get('enddate')

    Project.objects.filter(id=id).update(p_projectname=projectname, p_description=description, p_startdate=startdate,p_enddate=enddate)
    return JsonResponse({'status':1})


def updateProfile(request):
    id = request.POST.get('id')
    fname = request.POST.get('fname')
    mname  = request.POST.get('mname')
    lname  = request.POST.get('lname')
    email  = request.POST.get('email')
    phone  = request.POST.get('phone')
    gender  = request.POST.get('gender')
    bio  =  request.POST.get('bio')
    dob  =  request.POST.get('dob')
    occupation  = request.POST.get('occupation')
    country  = request.POST.get('country')
    region  = request.POST.get('region')
    file  = request.FILES.get('file')

    user_id  = request.user.id 
    cv_id = Cv.objects.filter(user_id=user_id).values_list('id',flat=True)
    cv_id = list(cv_id)
    cv_id = cv_id[0]

    Profile.objects.filter(cv_id=id).update(fname=fname, mname=mname,lname=lname,email=email, bio=bio, dob=dob, gender=gender, occupation=occupation, country=country, region=region, avator=file, phone=phone, cv_id=cv_id)
    return JsonResponse({'status':1})

def registerView(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = make_password(password)

        check_user = User.objects.filter(username=username).count()
        check_email = User.objects.filter(email=email).count()

        if(check_user>0):
            messages.error(request,'Username is already taken')
            return redirect('reg-form')
        elif(check_email>0):
            messages.error(request,'Email is a already taken')
            return redirect('reg_form')
        else:
            User.objects.create(username=username,email=email, password=password)
            messages.success(request,"Account created successfully, Please Sign In")
            return redirect('reg-form')
    else:
        return render(request,'core/register.html')

def logoutView(request):
    logout(request)
    return redirect('index')

def viewPDF(request,id=None):
    user_profile = Profile.objects.filter(cv_id=id)
    user_skill = Skill.objects.filter(cv_id=id).values()
    user_referee = Referee.objects.filter(cv_id=id).values()
    user_education = Academic.objects.filter(cv_id=id).values()
    user_experience = Experience.objects.filter(cv_id=id).values()
    user_project = Project.objects.filter(cv_id=id).values()

    context={'user_profile':user_profile,'user_skill':user_skill,'user_referee':user_referee,'user_education':user_education,'user_experience':user_experience,'user_project':user_project}
    return render(request,'core/pdf_template.html',context)

def editCv(request):
    return render(request,'core/edit_cv.html')

def fetchProfile(request):
    id=request.POST.get('id')
    print('Cv ID is',id)
    user_profile =Profile.objects.get(cv_id=id)

    user_profile={'fname':user_profile.fname,
                  'mname':user_profile.mname,
                  'lname':user_profile.lname,
                  'email':user_profile.email,
                  'phone':user_profile.phone,
                  'bio':user_profile.bio,
                  'dob':user_profile.dob,
                  'country':user_profile.country,
                  'region':user_profile.region,
                  'occupation':user_profile.occupation
                  }
    return JsonResponse(user_profile)

def fetchAcademic(request):
    id = request.POST.get('id')
    print('CV ID is',id)

    user_education = Academic.objects.get(id=id)
    
    user_education={'institution':user_education.a_institution,
                    'year':user_education.a_year,
                    'award':user_education.a_award
                    }
    return JsonResponse(user_education)

def fetchExperience(request):
    id = request.POST.get('id')
    print('CV ID is',id)

    user_experience = Experience.objects.get(id=id)
    
    user_experience={'office':user_experience.e_office,
                    'duration':user_experience.e_duration,
                    'position':user_experience.e_position
                    }
    return JsonResponse(user_experience)

def fetchProject(request):
    id = request.POST.get('id')
    print('CV ID is',id)

    user_project = Project.objects.get(id=id)
    
    user_project={'projectname':user_project.p_projectname,
                    'description':user_project.p_description,
                    'startdate':user_project.p_startdate,
                    'enddate':user_project.p_enddate
                    }
    return JsonResponse(user_project)


def fetchSkill(request):
    id = request.POST.get('id')
    print('Cv ID is',id)

    user_skill =Skill.objects.get(id=id)
    user_skill = {'name': user_skill.s_name,
                  'level': user_skill.s_level}
    return JsonResponse(user_skill)

def fetchReferee(request):
    id = request.POST.get('id')
    print('Cv ID is',id)

    user_referee =Referee.objects.get(id=id)
    user_referee = {'name': user_referee.r_name,
                    'phone':user_referee.r_phone,
                    'email': user_referee.r_email
                  }
    return JsonResponse(user_referee)


def deleteProfile(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        print('Cv ID is ',id)

        user_profile = Profile.objects.get(cv_id=id)
        user_profile.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def deleteSkill(request):
    if request.method == 'POST':
        id= request.POST.get('id')
        print('Cv ID is',id)

        user_skill = Skill.objects.get(id=id)
        user_skill.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    

def deleteReferee(request):
    if request.method == 'POST':
        id= request.POST.get('id')
        print('Cv ID is',id)

        user_referee = Referee.objects.get(id=id)
        user_referee.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0}) 

def deleteAcademic(request):
    if request.method == 'POST':
        id= request.POST.get('id')
        print('Cv ID is',id)

        user_education = Academic.objects.get(id=id)
        user_education.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    
def deleteExperience(request):
    if request.method == 'POST':
        id= request.POST.get('id')
        print('Cv ID is',id)

        user_experience = Experience.objects.get(id=id)
        user_experience.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    
    
def deleteProject(request):
    if request.method == 'POST':
        id= request.POST.get('id')
        print('Cv ID is',id)

        user_project = Project.objects.get(id=id)
        user_project.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})      

    
def educationView(request):
    id =request.user.cv.id 
    print('Cv ID is',id)
    user_education = Academic.objects.filter(cv_id=id).all()
    context = {'user_education':user_education}
    return render(request, 'core/education_view.html', context)

def experienceView(request):
    id =request.user.cv.id 
    print('Cv ID is',id)
    user_experience = Experience.objects.filter(cv_id=id).all()
    context = {'user_experience':user_experience}
    return render(request, 'core/experience_view.html', context)

def projectView(request):
    id =request.user.cv.id 
    print('Cv ID is',id)
    user_project = Project.objects.filter(cv_id=id).all()
    context = {'user_project':user_project}
    return render(request, 'core/project_view.html', context)

def skillView(request):
    id = request.user.cv.id
    print('Cv ID is', id)
    user_skill = Skill.objects.filter(cv_id=id).all()
    context = {'user_skill': user_skill}
    return render(request, 'core/skill_view.html', context)

def refereeView(request):
    id = request.user.cv.id
    print('Cv ID is', id)
    user_referee = Referee.objects.filter(cv_id=id).all()
    context = {'user_referee': user_referee}
    return render(request, 'core/referee_view.html', context)

def generate_PDF(request, id):
    print('Download Cv Id is', id)
    pdf = pdfkit.from_url(request.build_absolute_uri(
        reverse('cv-detail', args=[id])), False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response


    
    

        








   













