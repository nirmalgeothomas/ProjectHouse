from django.urls import re_path
from . import views

urlpatterns = [
    #admin dashboard
    re_path(r'^admindash$', views.adminDash, name='adminDash'),
    re_path(r'^abc$', views.abc, name='abc'),

    #admin login
    re_path(r'^admin_login/$', views.admin_login, name='admin_login'),
    re_path(r'^adminDash/deleteprofile/<int:id>$', views.deleteprofile,name='deleteprofile'),

    #intership
   
    #platform 

    #add platform 
    re_path(r'^platform$', views.platform, name='platform'),

    #display platform
    re_path(r'^mainplatform$', views.mainplatform, name='mainplatform'),

    #edit platform
    re_path(r'^mainplatform/editplatform/<int:id>$', views.editplatform, name='editplatform'),


    #update platform 
    re_path(r'^mainplatform/editplatform/updateplatform/<int:id>$', views.updateplatform, name='updateplatform'),

    #delete platform
    re_path(r'^mainplatform/deleteplatform/<int:id>$', views.deleteplatform,name='deleteplatform'),

    #profile
    re_path(r'^myprofile$', views.myprofile, name='myprofile'),

    #update profile
    re_path(r'^profileshow/<int:id>$', views.profileshow, name='profileshow'),

     
    #projects

    #projects mainpage 
    re_path(r'^projects$', views.projects, name='projects'),

    # display requested projects on admin side
    re_path(r'^reqprojects$', views.reqprojects, name='reqprojects'),
    re_path(r'^adminDashboard/reqprojects$', views.reqprojects, name='reqprojects'),

    #not working
    re_path(r'^viewprojects$', views.viewprojects, name='viewprojects'),

    #display platform 
    re_path(r'^viewprojectdetail/(?P<id>\d+)$', views.viewprojectdetail, name='viewprojectdetail'),
    re_path(r'^viewieeedetail/(?P<id>\d+)$', views.viewieeedetail, name='viewieeedetail'),
    re_path(r'^viewprojectdetails$', views.viewprojectdetails, name='viewprojectdetails'),
    re_path(r'^viewieeedetails$', views.viewieeedetails, name='viewieeedetails'),

    #Home Page
    re_path(r'^$',views.userdashboard, name='userdashboard'),

    #add project
    re_path(r'^addproject$', views.addproject, name='addproject'),

    #request project to admin 
    re_path(r'^userreqprojects$', views.userreqprojects, name='userreqprojects'),

    #display projects based on platform
    re_path(r'^userprojects/(?P<id>\d+)$', views.userpythonprojects, name='userpythonprojects'),
    
    re_path(r'^userpy$', views.userpy, name='userpy'),

    re_path(r'^adminprojectsview/(?P<id>\d+)$', views.adminprojectsview, name='adminprojectsview'),
    re_path(r'^adminprojectsviews/(?P<id>\d+)$', views.adminprojectsviews, name='adminprojectsviews'),

    #not working
    re_path(r'^userandroid$', views.userandroid, name='userandroid'),
    re_path(r'^usermlprojects$', views.usermlprojects, name='usermlprojects'),
    
    re_path(r'^userml$', views.userml, name='userml'),

    #display project details
    re_path(r'^userviewpython/(?P<id>\d+)$', views.userviewpython, name='userviewpython'),
    
    #save user request project
    re_path(r'^userreqprojects/userreqprojectdb$', views.userreqprojectdb, name='userreqprojectdb'),
    
    #delete projects
    re_path(r'^viewprojectdetail/deleteprojectss/(?P<id>\d+)$', views.deleteprojectss,name='deleteprojectss'),
    re_path(r'^viewprojectdetail/deleteprojects/(?P<id>\d+)$', views.deleteprojects,name='deleteprojects'),
    re_path(r'^Intermediate$', views.Intermediate,name='Intermediate'),

    #save project details
    re_path(r'^addproject/addnewprojectdb$', views.addnewprojectdb, name='addnewprojectdb'),

    #save platform details
    re_path(r'^platform/addnewplatformdb$', views.addnewplatformdb, name='addnewplatformdb'),

    #not working
    re_path(r'^viewmlproject/<int:id>', views.viewmlproject, name='viewmlproject'),
    re_path(r'^viewandroidproject/<int:id>', views.viewandroidproject, name='viewandroidproject'),
    re_path(r'^takeDiversion/<str:name>', views.ProjectDiverter, name='takeDiversion'),
    re_path(r'^viewmlprojects$', views.viewmlprojects, name='viewmlprojects'),
    re_path(r'^viewandroidprojects$', views.viewandroidprojects, name='viewandroidprojects'),

    #update profile
    re_path(r'^myprofile/profilecreate/<int:id>$', views.profilecreate, name='profilecreate'),

    # create a profile
    re_path(r'^myprofile/newprofilecreate$', views.newprofilecreate, name='newprofilecreate'),

    #not working
    re_path(r'^result$', views.result, name='result'),

    re_path(r'^getproject/(?P<id>\d+)$', views.getproject, name='getproject'),
    re_path(r'^show_inbuiltproject_requests$', views.show_inbuiltproject_requests, name='show_inbuiltproject_requests'),
    re_path(r'^user_show_ieeeproject$', views.user_show_ieeeproject, name='user_show_ieeeproject'),
    #search projects
    re_path(r'^search$',views.search,name='search'),

    re_path(r'^main_ieee$', views.main_ieee, name='main_ieee'),

    re_path(r'^main_ieee/deletepaper/(?P<id>\d+)$', views.deletepaper,name='deletepaper'),

    re_path(r'^add_ieee$', views.add_ieee, name='add_ieee'),

    re_path(r'^add_ieee_db$', views.add_ieee_db, name='add_ieee_db'),
    
    re_path(r'^req_ieeeprojects$', views.req_ieeeprojects, name='req_ieeeprojects'),
    
    re_path(r'^view_tutorials$', views.view_tutorials, name='view_tutorials'),
    re_path(r'^user_views$', views.user_views, name='user_views'),

    re_path(r'^view_ieee_papers/(?P<id>\d+)$', views.view_ieee_papers, name='view_ieee_papers'),

    re_path(r'^ieee_search$',views.ieee_search,name='ieee_search'),

    re_path(r'^user_req_ieee_projects/(?P<id>\d+)$', views.user_req_ieee_projects, name='user_req_ieee_projects'),

    re_path(r'^user_req_ieeeprojectdb$', views.user_req_ieeeprojectdb, name='user_req_ieeeprojectdb'),

    re_path(r'^req_ieee$', views.req_ieee, name='req_ieee'),

    re_path(r'^user_req_inbuilt_projectss/(?P<id>\d+)$', views.user_req_inbuilt_projectss, name='user_req_inbuilt_projectss'),

    re_path(r'^user_req_inbuilt_projectdbs$', views.user_req_inbuilt_projectdbs, name='user_req_inbuilt_projectdbs'),
    
    re_path(r'^userintership$', views.userintership, name='userintership'),

    re_path(r'^interview_q_a$', views.interview_q_a, name='interview_q_a'),

    re_path(r'^interview$', views.interview, name='interview'),

    re_path(r'^deleteq/<int:id>$', views.deleteq, name='deleteq'),

    re_path(r'^interview_Q_A$', views.interview_Q_A, name='interview_Q_A'),

    re_path(r'^admin_logout$', views.admin_logout, name='admin_logout'),

    re_path(r'^activate$', views.activate, name='activate'),

    re_path(r'^quiz$', views.quiz, name='quiz'),


    re_path(r'^savemockq$', views.savemockq, name='savemockq'),

    re_path(r'^usermockexam$', views.usermockexam, name='usermockexam'),

    re_path(r'^takemocktest$', views.takemocktest, name='takemocktest'),


    re_path(r'^deletequestion/<int:id>$', views.deletequestion, name='deletequestion'),

    re_path(r'^mailmeresult$', views.mailmeresult, name='mailmeresult'),

    re_path(r'^home$', views.home, name='home'),

    re_path(r'^viewtutorial$', views.viewtutorial, name='viewtutorial'),

    re_path(r'^addvediotutorial$', views.addvediotutorial, name='addvediotutorial'),

    re_path(r'^uploadtutorial$', views.uploadtutorial, name='uploadtutorial'),


    re_path(r'^delvediotutorial/<int:id>$', views.delvediotutorial, name='delvediotutorial'),


    re_path(r'^userviewtutorial$', views.userviewtutorial, name='userviewtutorial'),
    #courses module
    re_path(r'^courses$', views.courses, name='courses'),
    #Platform
    re_path(r'^platforms$', views.platforms, name='platform'),
    re_path(r'^addplatform$', views.addplatform, name='addplatform'),
    re_path(r'^addplatforms$', views.addplatforms, name='addplatforms'),
    re_path(r'^editplatform/(?P<id>\d+)$', views.editplatform, name='editplatform'),
    re_path(r'^updateplatform/(?P<id>\d+)$', views.updateplatform, name='updateplatform'),
    re_path(r'^deleteplatform/(?P<id>\d+)$', views.deleteplatform, name='deleteplatform'),
    #Courses
    re_path(r'^course$', views.course, name='course'),
    re_path(r'^addcoursepage$', views.addcoursepage, name='addcoursepage'),
    re_path(r'^addcourse$', views.addcourse, name='addcourse'),
    re_path(r'^editcourse/<int:courseid>$', views.editcourse, name='editcourse'),
    re_path(r'^updatecourse/<int:courseid>$', views.updatecourse, name='updatecourse'),
    re_path(r'^deletecourse/<int:courseid>$', views.deletecourse, name='deletecourse'),

    re_path(r'^lectures$', views.lectures, name='lectures'),
    re_path(r'^addlecturepage$', views.addlecturepage, name='addlecturepage'),
    re_path(r'^addlecture$', views.addlecture, name='addlecture'),
    re_path(r'^editlecture/<int:lectureid>$', views.editlecture, name='editlecture'),
    re_path(r'^updatelecture/<int:lectureid>$', views.updatelecture, name='updatelecture'),
    re_path(r'^deletelecture/<int:lectureid>$', views.deletelecture, name='deletelecture'),

    re_path(r'^questions$', views.questions, name='questions'),
    re_path(r'^addquestionpage$', views.addquestionpage, name='addquestionpage'),
    re_path(r'^addquestion$', views.addquestion, name='addquestion'),
    re_path(r'^editquestionpage/<int:qandaid>$', views.editquestionpage, name='editquestionpage'),
    re_path(r'^updatequestion/<int:qandaid>$', views.updatequestion, name='updatequestion'),
    re_path(r'^deletequestionanswer/<int:qandaid>$', views.deletequestionanswer, name='deletequestionanswer'),

    re_path(r'^usercreate$', views.usercreate, name='usercreate'),


    re_path(r'^gologins$', views.gologins, name='gologins'),


    re_path(r'^gosignup$', views.gosignup, name='gosignup'),

    re_path(r'^userlogin$', views.userlogin, name='userlogin'),
    re_path(r'^userdash$', views.userdash, name='userdash'),

    re_path(r'^userprofile$', views.userprofile, name='userprofile'),
    re_path(r'^tutorials$', views.tutorials, name='tutorials'),
   
    re_path(r'^tutorialview/<int:lectureid>$', views.tutorialview, name='tutorialview'),
    re_path(r'^userlogout$', views.userlogout, name='userlogout'),
    re_path(r'^edituserprofile/(?P<id>\d+)$',views.edituserprofile, name='edituserprofile'),
    re_path(r'^updateuserprofile/(?P<id>\d+)$',views.updateuserprofile, name='updateuserprofile'),
    re_path(r'^certificate$',views.certificate, name='certificate'),
    re_path(r'^test$',views.test, name='test'),
    re_path(r'^score1$', views.score1, name='score1'),
    re_path(r'^gocertificate$', views.gocertificate, name='gocertificate'),
    re_path(r'^gonocertificate$', views.gonocertificate, name='gonocertificate'),
    
    re_path(r'^intership$', views.intership, name='intership'),

#user module
    re_path(r'^userlog$', views.userlog, name='userlog'),
    re_path(r'^userreg$', views.userreg, name='userreg'),
    
]
