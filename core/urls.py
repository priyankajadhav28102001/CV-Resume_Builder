from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('login/', views.loginView, name= "login"),
    path('logout/', views.logoutView, name= "logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('createcv/', views.createCv, name="createcv"),
    path('skill-save/', views.saveSkill, name="skill-save"),
    path('edu-save/', views.saveEducation, name="edu-save"),
    path('exp-save/', views.saveExperience, name="exp-save"),
    path('cer-save/', views.saveCertificate, name="cer-save"),
    path('pro-save/', views.saveProject, name="pro-save"),
    path('ref-save/', views.saveReferee, name="ref-save"),
    path('profile-save/', views.uploadProfile, name="profile-save"),
    path('register/', views.registerView, name="reg-form"),
    path('cv-detail/<id>', views.viewPDF, name="cv-detail"),
    path('cv-download/<id>', views.generate_PDF, name="cv-download"),
    path('cv-edit/', views.editCv, name="cv-edit"),

    #^    Profile fetch,update,delete
    path('cv-edit/fetchprofile/', views.fetchProfile, name="fetchprofile"),
    path('cv-edit/updateprofile/', views.updateProfile, name="profile-update"),
    path('cv-edit/deleteprofile/', views.deleteProfile, name="profile-delete"),

     #^    Education fetch,update,delete
    path('cv-edit/eduview/', views.educationView, name="edu-view"),
    path('cv-edit/eduview/academic/', views.fetchAcademic, name="fetchacademic"),
    path('cv-edit/eduview/update_academic/', views.updateAcademic, name="update_academic"),
    path('cv-edit/eduview/delete_academic/', views.deleteAcademic, name="delete_academic"),

    #^    Experience fetch,update,delete
    path('cv-edit/expview/', views.experienceView, name="exp-view"),
    path('cv-edit/expview/experience/', views.fetchExperience, name="fetchexperience"),
    path('cv-edit/expview/update_experience/', views.updateExperience, name="update_experience"),
    path('cv-edit/expview/delete_experience/', views.deleteExperience, name="delete_experience"),

    #^    skills fetch update,delete
    path('cv-edit/skillview/', views.skillView, name="skill-view"),
    path('cv-edit/skillview/skill/', views.fetchSkill, name="fetchskill"),
    path('cv-edit/skillview/update_skill/', views.updateSkill, name="update_skill"),
    path('cv-edit/skillview/delete_skill/', views.deleteSkill, name="delete_skill"),

    #^    referees fetch update,delete
    path('cv-edit/refview/', views.refereeView, name="ref-view"),
    path('cv-edit/refview/referee/', views.fetchReferee, name="fetchreferee"),
    path('cv-edit/refview/update_referee/', views.updateReferee, name="update_referee"),
    path('cv-edit/refview/delete_referee/', views.deleteReferee, name="delete_referee"),

    #^    Project fetch,update,delete
    path('cv-edit/proview/', views.projectView, name="pro-view"),
    path('cv-edit/proview/project/', views.fetchProject, name="fetchproject"),
    path('cv-edit/proview/update_project/', views.updateProject, name="update_project"),
    path('cv-edit/proview/delete_project/', views.deleteProject, name="delete_project"),

    #^    Certificate fetch,update,delete
    path('cv-edit/cerview/', views.certificateView, name="cer-view"),
    path('cv-edit/cerview/certificate/', views.fetchCertificate, name="fetchcertificate"),
    path('cv-edit/cerview/update_certificate/', views.updateCertificate, name="update_certificate"),
    path('cv-edit/cerview/delete_certificate/', views.deleteCertificate, name="delete_certificate"),


]