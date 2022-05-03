import os
from django.db.models import Q
from django.shortcuts import render, redirect
import json
from Administrator.models import *
from django.http import JsonResponse, HttpResponse
from django.views.defaults import page_not_found
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from Administrator.otpgen import gen_otp

from django.core.mail import send_mail
from Administrator.otpgen import send_sms,gen_otp
import random
from django.contrib.auth.models import User, auth

# Create your views here.
random_otp =gen_otp()

def abc(request):
    return render(request, 'Administrator/dashboard.html')
#admin login
def admin_login(request):
    if request.method == "POST":
        user1 = request.POST['username']
        pass1 = request.POST['password']
        if profile.objects.filter(name=user1).exists():
            if profile.objects.filter(password=pass1, name=user1).exists():
                request.session['admin'] = user1
                pro = profile.objects.all()
                project = Addnewproject.objects.all().count()
                platform = Addnewplatform.objects.all().count()
                proreq = Userrequestproject.objects.all().count()
                requestedpro = User_req_inbuilt_project.objects.all().count()
                return render(request, 'Administrator/dashboard.html',
                              {'profile': pro, 'project': project, 'platform': platform, 'proreq': proreq,
                               'requestedpro': requestedpro})
            else:
                messages.info(request,'invalid password')
                return render(request, 'Administrator/login.html')
        else:
            messages.info(request, 'invalid userid')
            return render(request, 'Administrator/login.html')
    else:
        return render(request, 'Administrator/login.html')

def admin_logout(request):
    try:
        del request.session['admin']
    except:
        return redirect('admin_login')
    return redirect('admin_login')


#intership
def intership(request):
    if 'admin' in request.session:
        platform = applyintershipt.objects.all()
        verify=PhoneOtp.objects.all()
        return render(request, 'Administrator/intershiprequest.html',{'platform':platform, 'verify':verify})
    else:
        return redirect('admin_login')
#admin  after login or admin Dashboard

def adminDash(request):  # dashboard
    if 'admin' in request.session:
        pro = profile.objects.all()
        project = Addnewproject.objects.all().count()
        platform = Addnewplatform.objects.all().count()
        proreq = Userrequestproject.objects.all().count()
        requestedpro = User_req_inbuilt_project.objects.all().count()
        return render(request, 'Administrator/dashboard.html',
                      {'profile': pro, 'projects': project, 'platform': platform, 'proreq': proreq,
                               'requestedpro': requestedpro})
    else:
        return redirect('admin_login')

#platform

#add platform
def platform(request):
    return render(request, 'Administrator/add new platform.html')

#display platform
def mainplatform(request):
    if 'admin' in request.session:
        platform = Addnewplatform.objects.all()
        return render(request, 'Administrator/main_platform.html', {'plat': platform})
    else:
        return redirect('admin_login')

def editplatform(request, id):
    plat1 = Addnewplatform.objects.get(id=id)
    context = {'platform': plat1}
    return render(request, 'Administrator/edit platform.html', context)

#update platform 
def updateplatform(request,id):
    plat1 = Addnewplatform.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(plat1.uploadthumbnail)>0:
                os.remove(plat1.uploadthumbnail.path)
            plat1.uploadthumbnail = request.FILES['thumbimg']
    plat1.platformname = request.POST['platformname']
    plat1.description = request.POST['description']
    plat1.save()
    return render(request, 'Administrator/dashboard.html', )

#delete platform 
def deleteplatform(request, id):
    plat = Addnewplatform.objects.get(id=id)
    plat.delete()
    return redirect('adminDash')

#profile
def myprofile(request):
    if 'admin' in request.session:
        user1 = request.session['admin']
        pro1 = profile.objects.get(name=user1)
        pro = profile.objects.filter(id=pro1.id)
        return render(request, 'Administrator/my_profile.html',
                  {'profile': pro})
    else:
        return redirect('admin_login')

#main project page
def projects(request):
    if 'admin' in request.session:
        return render(request, 'Administrator/projects.html')
    else:
        return redirect('admin_login')


def viewprojects(request):
    return render(request, 'Administrator/view projects.html')

#display projects platform name
def viewprojectdetail(request, id):
    plat = Addnewplatform.objects.all()
    project = add_new_ieee.objects.all()
    context = {'plat': plat, 'project': project}
    return render(request, 'Administrator/view_projects_detail.html', context)

def viewieeedetail(request, id):
    plat = Addnewplatform.objects.all()
    project = add_new_ieee.objects.all()
    context = {'plat': plat, 'project': project}
    return render(request, 'Administrator/viewieeedetail.html', context)

def viewprojectdetails(request):
    plat = Addnewplatform.objects.all()
    project = Addnewproject.objects.all()
    context = {'plat': plat, 'project': project}
    return render(request, 'Administrator/view_projects_detail.html', context)

def viewieeedetails(request):
    plat = Addnewplatform.objects.all()
    project = add_new_ieee.objects.all()
    context = {'plat': plat, 'project': project}
    return render(request, 'Administrator/viewieeedetails.html', context)

#home page display
def userdashboard(request):
    if request.method == 'POST':
        searchQuery = request.POST['search']
        print(searchQuery)
        print(type(searchQuery))
        data = []
        if searchQuery != '':
            searchResult = Addnewproject.objects.filter(projectname__icontains=searchQuery).values()
            print(searchResult)

            searchResultant = Addnewproject.objects.filter(projectname__icontains=searchQuery)
            for x in searchResultant:
                data.append(x.projectname)
            print(data)

        else:
            searchResult = 'Type something to search'
        return JsonResponse(data, safe=False)

    else:
        platform_name = Addnewplatform.objects.all()
        quest = Q_A.objects.all()
        plat = {'platform_name': platform_name,'quest':quest}
        return render(request, 'Administrator/user_dasboard.html', plat)

#add project
def addproject(request):
    projectname = Addnewproject.objects.all()
    platformname = Addnewplatform.objects.all()
    projectname_count = projectname.count()
    context = {'projectname': projectname, 'projectname_count': projectname_count, 'platformname': platformname}
    return render(request, 'Administrator/add_new_project.html', context)


#display projects based on platform
def userpythonprojects(request, id):
    plat = Addnewplatform.objects.filter(id=id)
    plat1 = Addnewplatform.objects.get(id=id)
    project = Addnewproject.objects.filter(selectplatform=plat1.platformname)
    context = {'plat': plat, 'projects': project}
    return render(request, 'Administrator/user_projects.html', context)

#idsplay projects on platform on view projects page
def adminprojectsview(request, id):
    mem = Addnewplatform.objects.get(id=id).platformname
    print(mem)
    if request.method != 'POST':
        plat = Addnewplatform.objects.all()
        project = Addnewproject.objects.filter(selectplatform=mem)
       
        return render(request, 'Administrator/view_projects_detail.html', {'plat':plat,'project':project})
    else:
        return render(request, 'Administrator/dashboard.html')

def adminprojectsviews(request, id):
    mem = Addnewplatform.objects.get(id=id).platformname
    print(mem)
    if request.method != 'POST':
        plat = Addnewplatform.objects.all()
        project = Addnewproject.objects.filter(selectplatform=mem)
       
        return render(request, 'Administrator/view_projects_detail.html', {'plat':plat,'project':project})
    else:
        return render(request, 'Administrator/dashboard.html')

#not working
def userml(request):  # userprojects
    project = Addnewproject.objects.filter(selectplatform='Machine Learning')
    context = {'projects': project}
    return render(request, 'Administrator/user ml projects.html', context)

def userpy(request):  # userprojects
    project = Addnewproject.objects.filter(selectplatform='Python')
    context = {'projects': project}
    return render(request, 'Administrator/user python projects.html', context)

def userandroid(request):  # userprojects
    project = Addnewproject.objects.filter(selectplatform='Android')
    context = {'projects': project}
    return render(request, 'Administrator/user android projects.html', context)

#not working
def usermlprojects(request):
    if request.method != 'POST':
        project = Addnewproject.objects.filter(selectplatform='Machine Learning')
        context = {'projects': project}
        return render(request, 'Administrator/user ml projects.html', context)
    else:
        return render(request, 'Administrator/user_dasboard.html')

#not working
def ProjectDiverter(request, name):
    print(name)
    if Addnewproject.objects.filter(projectname=name).exists():
        projects = Addnewproject.objects.filter(projectname=name)
        for project in projects:
            if project.selectplatform == 'Python':
                context = {'projects': projects}
                return render(request, 'Administrator/user python projects.html', context)
            if project.selectplatform == 'ML':
                context = {'projects': projects}
                return render(request, 'Administrator/user ml projects.html', context)
            if project.selectplatform == 'Android':
                context = {'projects': projects}
                return render(request, 'Administrator/user android projects.html', context)
    else:
        return page_not_found(request)

#display each projects details
def userviewpython(request, id):
    if request.method == 'POST':
        return render(request, 'Administrator/user dasboard.html')

    else:
        project = Addnewproject.objects.get(id=id)

        context = {'projects': project}
        return render(request, 'Administrator/user view python projects.html', context)

#delete projects
def deleteprojects(request, id):
    dela = Addnewproject.objects.get(id=id)
    dela.delete()
    return redirect('adminDash')

def deleteprojectss(request, id):
    dela = Addnewproject.objects.get(id=id)
    dela.delete()
    return redirect('adminDash')

def Intermediate(request):
    return render(request,'user/intermidiate.html')
#save projects
def addnewprojectdb(request):
    if request.method == 'POST':
        projectname = request.POST['projectname']
        price = request.POST['price']
        shortdescription = request.POST['shortdescription']
        uploadthumbnail = request.FILES.get('uploadthumbnail')
        selectplatform = request.POST['selectplatform']
        languageused = request.POST['languageused']
        database = request.POST['database']
        softwares = request.POST['softwares']
        userinterface = request.POST['userinterface']
        projectabstract = request.POST['projectabstract']
        moduledetails = request.POST['moduledetails']
        uploadvideo = request.FILES.get('uploadvideo')
        uploadscreenshots = request.FILES.get('uploadscreenshots')
        uploadscreenshots1 = request.FILES.get('uploadscreenshots1')
        uploadscreenshots2 = request.FILES.get('uploadscreenshots2')
        uploadscreenshots3 = request.FILES.get('uploadscreenshots3')
        uploadpdf = request.FILES.get('uploadpdf')

        pro = Addnewproject.objects.create(projectname=projectname,price=price, shortdescription=shortdescription,
                                           uploadthumbnail=uploadthumbnail,
                                           selectplatform=selectplatform, languageused=languageused,
                                           database=database, softwares=softwares, userinterface=userinterface,
                                           projectabstract=projectabstract,
                                           moduledetails=moduledetails, uploadvideo=uploadvideo,
                                           uploadscreenshots=uploadscreenshots, uploadscreenshots1=uploadscreenshots1,
                                           uploadscreenshots2=uploadscreenshots2,
                                           uploadscreenshots3=uploadscreenshots3, uploadpdf=uploadpdf)
        print(projectabstract)
        return redirect('adminDash')
    else:
        return render(request, 'Administrator/dashboard.html')

#save platform
def addnewplatformdb(request):
    if request.method == 'POST':
        platformname = request.POST['platformname']
        uploadthumbnail1 = request.FILES['thumbimg']
        description = request.POST['description']
        plat = Addnewplatform(platformname=platformname, uploadthumbnail=uploadthumbnail1, description=description)
        plat.save()
        return redirect('adminDash')
    else:
        return render(request, 'Administrator/dashboard.html')

#not working
def viewmlproject(request, id):
    if request.method == 'POST':
        return render(request, 'Administrator/user_dasboard.html')

    else:
        project = Addnewproject.objects.get(id=id)

        context = {'projects': project}
        return render(request, 'Administrator/view user ml projects.html', context)

#not working
def viewandroidproject(request, id):
    if request.method == 'POST':
        return render(request, 'Administrator/user_dasboard.html')

    else:
        project = Addnewproject.objects.get(id=id)

        context = {'projects': project}
        return render(request, 'Administrator/user view android projects.html', context)

#search projects
def search(request):
    if request.method == 'POST':
        usr = request.POST['search']
        pro = Q(projectname__icontains=usr)|Q(languageused__icontains=usr)|Q(shortdescription__icontains=usr)
        dsa = Addnewproject.objects.filter(pro).distinct()
        context = {'projects': dsa}
        return render(request, 'Administrator/search.html', context)

#not working
def viewmlprojects(request):
    return render(request, 'Administrator/view ml projects.html')

#not working
def viewandroidprojects(request):
    return render(request, 'Administrator/view android.html')

#edit admin profile 
def profilecreate(request,id):
    dela = profile.objects.get(id=id)
    dela.name=request.POST['name']
    dela.phone=request.POST['phone']
    dela.email=request.POST['email'],
    dela.password=request.POST['password']
    dela.save()
    return redirect('adminDash')

#create admin profile
def newprofilecreate(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email'],
    password = request.POST['password']
    getpro = profile.objects.create(name=name, email=email, phone=phone,password=password)
    getpro.save()
    return render(request, 'Administrator/dashboard.html', )

#delete admin profile
def deleteprofile(request, id):
    delpro = profile.objects.get(id=id)
    delpro.delete()
    return render(request, 'Administrator/dashboard.html')


def profileshow(request,id):
    pro = profile.objects.get(id=id)
    context = {'profile': pro}
    return render(request, 'Administrator/my profile.html', context)


def result(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        value = Userrequestproject.objects.filter(name=q)
        context = {'name': value}
        return render(request, 'Administrator/requested_projects.html', context)
    else:
        return page_not_found(request)

#new project request
def reqprojectss(request):
    if 'admin' in request.session:
        req1 = Userrequestproject.objects.all()
        return render(request, 'Administrator/requested_projects.html', {'req': req1})
    else:
        return redirect('admin_login')
    # return render(request, 'Administrator/requested_projects.html')

def reqprojects(request):
    if 'admin' in request.session:
        req1 = Userrequestproject.objects.all()
        return render(request, 'Administrator/requested_projects.html', {'req': req1})
    else:
        return redirect('admin_login')


def userreqprojectdb(request):
    if request.method == 'POST':
        
        name = request.POST['name']
        emailid = request.POST['emailid']
        phonenumber = request.POST['phonenumber']
        projectname = request.POST['projectname']
        projectdescription = request.POST['projectdescription']
        project_zip = request.FILES['project_files']
        req2 = Userrequestproject.objects.create(name=name, emailid=emailid, phonenumber=phonenumber,
                                                projectname=projectname, projectdescription=projectdescription,project_file=project_zip)
        req2.save()
        messages.success(request,'Thank you, Admin will get to you soon')
        return redirect('userreqprojects')


def userreqprojects(request):
    req1 = Userrequestproject.objects.all()
    context = {'req': req1}
    return render(request, 'Administrator/user_request_projects.html', context)


def getproject(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        project = Addnewproject.objects.get(id=id)
        getpro = GetProject.objects.create(name=name, email=email, phone=phone, project_Detail=project)
        getpro.save()
    return redirect('userdashboard')


def show_inbuiltproject_requests(request):
    spro = User_req_inbuilt_project.objects.all()
    return render(request, 'Administrator/getreq_inbuiltprojects.html', {'spo': spro})

def user_show_ieeeproject(request):
    spro = User_req_ieeeproject.objects.all()
    return render(request, 'user/user_show_ieeeproject.html', {'spo': spro})

def req_ieee(request):
    return render(request, 'Administrator/req_ieeeproject.html')

def main_ieee(request):
    if 'admin' in request.session:
        ieee = add_new_ieee.objects.all()
        return render(request,'Administrator/main_ieee.html',{'paper':ieee})
    else:
        return redirect('admin_login')


def deletepaper(request,id):
    paper=add_new_ieee.objects.get(id=id)
    paper.delete()
    return redirect('adminDash')




def add_ieee(request):
    
    platformname=Addnewplatform.objects.all()
    context={'platformname':platformname}
    return render(request, 'Administrator/add_new_ieee.html',context)

def add_ieee_db(request):
    if request.method=="POST":
        title=request.POST["title"]
        selectplatform = request.POST['selectplatform']
        uploadpdf = request.FILES.get('uploadpdf')
        paper=add_new_ieee.objects.create(title=title,selectplatform=selectplatform,uploadpdf=uploadpdf)
        paper.save()
        return redirect('adminDash')
    else:
        return render(request,'Administrator/add new ieee.html')


def view_ieee_papers(request,id):
    mem = Addnewplatform.objects.get(id=id).platformname
    print(mem)
    if request.method != 'POST':
        plat = Addnewplatform.objects.get(id=id)
        paper = add_new_ieee.objects.filter(selectplatform=mem)
        context = {'paper': paper, 'plat': plat}
        return render(request, 'Administrator/view_ieee_papers.html', context)
    else:
        return render(request, 'Administrator/user_dasboard.html')

def ieee_search(request):
    if request.method == 'POST':
        usr = request.POST['ieeesearch']
        paper = Q(title__icontains=usr)
        dsa = add_new_ieee.objects.filter(paper).distinct()
        context = {'paper': dsa}
        return render(request, 'Administrator/ieee_search.html', context)
        
def user_req_ieee_projects(request,id):
    requested_paper=add_new_ieee.objects.get(id=id)
    context = {'requested_paper': requested_paper}
    return render(request, 'Administrator/user_request_ieee_projects.html', context)

def user_req_ieeeprojectdb(request):
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['emailid']
        phonenumber = request.POST['phonenumber']
        projectname = request.POST['projectname']
        location = request.POST['location']
        req2 = User_req_ieeeproject.objects.create(name=name, emailid=emailid, phonenumber=phonenumber,
                                                 projectname=projectname, Location=location)
        req2.save()
        messages.success(request,'Thank you, Admin will get to you soon')
    return render(request,'Administrator/user_request_ieee_projects.html')

def req_ieeeprojects(request):
    if 'admin' in request.session:
        req1 = User_req_ieeeproject.objects.all()
        return render(request, 'Administrator/requested_ieee_projects.html', {'req': req1})
    else:
        return redirect('admin_login')


def user_req_projectdb(request):
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['emailid']
        phonenumber = request.POST['phonenumber']
        projectname = request.POST['projectname']
        location = request.POST['location']
        req2 = User_req_inbuilt_project.objects.create(name=name, emailid=emailid, phonenumber=phonenumber,
                                                 projectname=projectname, Location=location)
        req2.save()
    return redirect('userdashboard')


def user_req_inbuilt_projectss(request,id):
    requested_paper=Addnewproject.objects.get(id=id)
    context = {'requested_paper': requested_paper}
    return render(request, 'Administrator/user_request_inbuilt_projects.html', context)

def user_req_inbuilt_projectdb(request):
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['emailid']
        phonenumber = request.POST['phonenumber']
        projectname = request.POST['projectname']
        location = request.POST['location']
        req2 = User_req_inbuilt_project.objects.create(name=name, emailid=emailid, phonenumber=phonenumber,
                                                 projectname=projectname, Location=location)
        req2.save()
        messages.success(request,'Thank you, Admin will get to you soon')
    return render(request,'Administrator/user_request_inbuilt_projects.html')

def user_req_inbuilt_projectdbs(request):
    if request.method == 'POST':
        name = request.POST['name']
        emailid = request.POST['emailid']
        phonenumber = request.POST['phonenumber']
        projectname = request.POST['projectname']
        location = request.POST['location']
        req2 = User_req_inbuilt_project.objects.create(name=name, emailid=emailid, phonenumber=phonenumber,
                                                 projectname=projectname, Location=location)
        req2.save()
        messages.success(request,'Thank you, Admin will get to you soon')
    return render(request,'Administrator/user_request_inbuilt_projects.html')

def userintership(request):
    if request.method == 'POST':
        account_sid="AC8fc1f29aa02f3a6e9beec28e3f7efc82"
        auth_token="f5a29b6452cb4f75e795e54488fb2541"
       
        name = request.POST['name']
        emailid = request.POST['emailid']
        phonenumber = request.POST['phonenumber']
        ssl = request.POST['selectplatform']
        qqa= request.POST['qualifications']
        aaq = request.POST['location']
        college=request.POST['college']
        '''req2 = applyintershipt.objects.create(name=name, emailid=emailid, phonenumber=phonenumber,
                                                 platform=ssl, qualifications=qqa,location=aaq,college=college)
        req2.save()'''

        request.session["a"] = name
        request.session["b"] = emailid
        request.session["c"] = phonenumber
        request.session["d"] = ssl
        request.session["e"] = qqa
        request.session["f"] = aaq
        request.session["g"] = college
        subject=ssl
        message=  "Greeting" + " " + name +"\n"+ "Thank you for contacting us your verification code is"+str(random_otp)
        recepient=str(emailid)
        send_mail(
            subject,message,EMAIL_HOST_USER,[recepient],fail_silently=False)
        messages.success(request, 'Please verify your application with the code that is sent to your registered email account.   ')
        msg_body=f'''Verify your internship application. Your verification code is {random_otp}
       '''
        '''send_sms(account_sid,auth_token, msg_body,'+14159972855', phonenumber)
        platformname = Addnewplatform.objects.all()'''
        return render(request, 'Administrator/activate.html')
    else:
        platformname = Addnewplatform.objects.all()
        return render(request, 'Administrator/userapplyintership.html',{'platformname':platformname})

def interview_q_a(request):
    if 'admin' in request.session:
        plat = Addnewplatform.objects.all()
        s=Q_A.objects.all()
        return render(request,'Administrator/admin_interview_Q_A.html',{'s':s,'plat':plat})
    else:
        return redirect('admin_login')

def interview(request):
    if request.method == 'POST':
        plat = request.POST['selectplatform']
        q1 = request.POST['qu1']
        a1 = request.POST['ans1']
        inte = Q_A.objects.create(q1=q1,a1=a1,platform_name=plat)
        inte.save()
        return redirect('interview_q_a')
def deleteq(request,id):
    re = Q_A.objects.get(id=id)
    re.delete()
    return redirect('interview_q_a')

def interview_Q_A(request):
    plat = Addnewplatform.objects.all()
    s = Q_A.objects.all()
    return render(request, 'Administrator/user_interview_questions.html', {'s': s, 'plat': plat})

def activate(request):
    name = request.session["a"]
    emailid = request.session["b"]
    phonenumber = request.session["c"]
    ssl = request.session["d"]
    qqa = request.session["e"]
    aaq = request.session["f"]
    college = request.session["g"]
    if request.method=="POST":
        otp_verify=request.POST["otp_verify"]
        if random_otp ==otp_verify:
            req2 = applyintershipt.objects.create(name=name, emailid=emailid, phonenumber=phonenumber,
                                                             platform=ssl, qualifications=qqa,location=aaq,college=college)
            req2.save()
            subject = ssl
            message = "Greeting" + " " + name + "\n" + "Your application has been verified. We will be contacting you soon."
            recepient = str(emailid)
            send_mail(
                subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            messages.success(request,'The submitted code has been verified. We will be contacting you soon.')
            return render(request,'Administrator/activate.html')
        else:
            messages.error(request,'Invalid code submitted. Please try again.')
            return render(request,'Administrator/activate.html')
    else:
        return render(request,'Administrator/activate.html')





  


def quiz(request):
    if 'admin' in request.session:
        plat = Addnewplatform.objects.all()
        s = QuesModel.objects.all()
        return render(request, 'Administrator/quizamin.html', {'plat': plat,'s': s})
    else:
        return redirect('admin_login')


def savemockq(request):
    if request.method == 'POST':
        plat = request.POST['selectplatform']
        q1 = request.POST['qu1']
        a1 = request.POST['choice1']
        a2 = request.POST['choice2']
        a3 = request.POST['choice3']
        a4 = request.POST['choice4']
        aa = request.POST['answer']
        inte = QuesModel.objects.create(platform_name=plat,question=q1,op1=a1,op2=a2,op3=a3,op4=a4,ans=aa)
        inte.save()
        return redirect('quiz')
    plat = Addnewplatform.objects.all()
    return render(request, 'Administrator/quizamin.html', {'plat': plat})


def deletequestion(request,id):
    re =QuesModel.objects.get(id=id)
    re.delete()
    plat = Addnewplatform.objects.all()
    s = QuesModel.objects.all()
    return render(request, 'Administrator/quizamin.html', {'plat': plat, 's': s})

def usermockexam(request):
    platformname = Addnewplatform.objects.all()
    return render(request, 'Administrator/Takemocktest.html',{'platformname':platformname})
def takemocktest(request):
    if request.method == 'POST':
        plat = request.POST['selectplatform']
        print(plat)
        # questions = QuesModel.objects.filter(platform_name=plat)
        items = list(QuesModel.objects.filter(platform_name=plat).order_by('id')[:10])
        random.shuffle(items)
        # print(questions)
        return render(request, 'Administrator/exam.html',{'questions': items,'plat':plat})
def home(request):
    if request.method == 'POST':
        print(request.POST)
        plat = request.POST['plat']
        print(plat)
        questions = QuesModel.objects.filter(platform_name=plat)
        score = 0
        wrong = 0
        correct = 0
        total = 0
        skipped=0
        wq=[]
        option5='option5'
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                if option5 == request.POST.get(q.question):
                    skipped +=1
                else:
                    wrong += 1
                    wq.append(total)
        res=str(wq)[1:-1]
        print(res)
        percent = score / (total * 10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'skipped':skipped,
            'total': total,
            'wronganswers':res
        }
        return render(request, 'Administrator/result.html', context)

def mailmeresult(request):
    s= request.GET.get('percentage')
    emailid= request.GET.get('email')
    subject="Result"
    message=   "Thank you for attending exam "+ "\n"+ "your score is " +str(s)
    recepient=str(emailid)
    send_mail(
            subject,message, EMAIL_HOST_USER,[recepient],fail_silently=False)
    print(s)
    return render(request, 'Administrator/result.html')

def viewtutorial(request):
    platformname = Addnewplatform.objects.all()
    return render(request, 'Administrator/tutorilsusermain.html', {'platformname': platformname})

def addvediotutorial(request):
    platformname = Addnewplatform.objects.all()
    tuto = tutorial.objects.all()
    return render(request, 'Administrator/adminaddvediotutorials.html', {'plat': platformname,'tutorial':tuto})

def uploadtutorial(request):
    if request.method == 'POST':
        plat = request.POST['selectplatform']
        title = request.POST['title']
        uploadvideo = request.FILES.get('uploadvideo')
        getpro = tutorial.objects.create(platform_name=plat,videotitle=title,uploadvideo=uploadvideo)
        getpro.save()
        platformname = Addnewplatform.objects.all()
        tuto = tutorial.objects.all()
        return render(request, 'Administrator/adminaddvediotutorials.html', {'plat': platformname,'tutorial':tuto})



def delvediotutorial(request,id):
    if 'admin' in request.session:
        re = tutorial.objects.get(id=id)
        re.delete()
        platformname = Addnewplatform.objects.all()
        tuto = tutorial.objects.all()
        return render(request, 'Administrator/adminaddvediotutorials.html', {'plat': platformname, 'tutorial': tuto})
    else:
        return redirect('admin_login')

def userviewtutorial(request):
    if request.method == 'POST':
        plat = request.POST['selectplatform']
        platformm=Addnewplatform.objects.get(platformname=plat)
        try:
            re = tutorial.objects.filter(platform_name=plat)[0]
        except:
            re="none"
        try:
            re1 = tutorial.objects.filter(platform_name=plat)[1]
        except:
            re1="none"
        try:
            re2 = tutorial.objects.filter(platform_name=plat)[2]
        except:
            re2="none"
        try:
            re3 = tutorial.objects.filter(platform_name=plat)[3]
        except:
            re3 = "none"
        try:
            re4 = tutorial.objects.filter(platform_name=plat)[4]
        except:
            re4 = "none"
        return render(request, 'Administrator/tutorialdisplay userside.html',
                  {'tutorial': re,'tutorial2':re1,'tutorial3':re2,'tutorial4':re3,'tutorial5':re4,'platform':platformm})


def courses(request):
    if 'admin' in request.session:
        return render(request, 'Administrator/courses.html')
    else:
        return redirect('admin_login')


def platforms(request):
    if 'admin' in request.session:
        if request.method == 'POST':
            mem3 = Addnewplatform()
            mem3.platformname= request.POST['platform_name']
            mem3.uploadthumbnail = request.FILES['upload_img']
            mem3.description = request.POST['platform_description']
            mem3.tutorial_discription = request.POST['tutorial_discription']
            mem3.tutorial_video= request.FILES['tutorial_video']

            

            mem3.save()
        return render(request, 'administrator/platforms.html')
    else:
        return redirect('admin_login')

def view_tutorials(request):
    
       var =Addnewplatform.objects.all()

       return render(request, 'user/view_tutorial.html',{'var':var})

def user_views(request):
    if request.method == 'POST':

        tut = request.POST['selectplatform']
        vars=Addnewplatform.objects.filter(id=tut)
        vars1=Addnewplatform.objects.get(id=tut)
        mem=Addnewplatform.objects.filter(platformname=vars1.platformname)
        

        return render(request, 'user/user_view.html',{'vars':vars,'mem':mem})
    # return render(request, 'user/user_view.html',{'vars':vars})


def addplatform(request):
    if 'admin' in request.session:
        return render(request, 'Administrator/addplatform.html')
    else:
        return redirect('admin_login')


def editplatform(request, platformid):
    if 'admin' in request.session:
        plat = Platform.objects.get(platformid=platformid)
        return render(request, 'Administrator/editplatform.html', {'platform': plat})
    else:
        return redirect('admin_login')


def addplatforms(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            if Platform.objects.filter(name=name):
                messages.info(request, f'Platform named {name} already exists')
                return redirect('addplatform')
            else:
                plat = Platform(name=name, description=description)
                plat.save()
                return redirect('platforms')
        else:
            return redirect('addplatform')
    except:
        return redirect('addplatform')


def updateplatform(request, platformid):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            plat = Platform.objects.get(platformid=platformid)
            plat.name = name
            plat.description = description
            plat.save()
            return redirect('platforms')
        else:
            return redirect('editplatform')
    except:
        return redirect('editplatform')


def deleteplatform(request, platformid):
    plat = Platform.objects.get(platformid=platformid)
    plat.delete()
    return redirect('platforms')


def course(request):
    if 'admin' in request.session:
        cour = Course.objects.all()
        return render(request, 'Administrator/course.html', {'course': cour})
    else:
        return redirect('admin_login')
    


def addcoursepage(request):
    if 'admin' in request.session:
        plat = Platform.objects.all()
        return render(request, 'Administrator/addcourse.html', {'platform': plat})
    else:
        return redirect('admin_login')


def addcourse(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            shortdescription = request.POST['shortdescription']
            try:
                description = request.FILES['description']
            except:
                description = ''
            modules = request.POST['modules']
            level = request.POST['level']
            platform = request.POST['platform']
            if Course.objects.filter(name=name, level=level):
                messages.info(request, 'Course already exists.')
                return redirect('addcoursepage')
            else:
                plat = Platform.objects.get(name=platform)
                cour = Course(name=name, shortdescription=shortdescription, description=description, modules=modules, level=level, platformid=plat)
                cour.save()
                return redirect('course')
        else:
            return redirect('addcoursepage')
    except:
        return redirect('addcoursepage')


def editcourse(request, courseid):
    if 'admin' in request.session:
        cour = Course.objects.get(courseid=courseid)
        plat = Platform.objects.all()
        return render(request, 'Administrator/editcourse.html', {'course': cour, 'platform': plat})
    else:
        return redirect('admin_login')


def updatecourse(request, courseid):
    try:
        if request.method == 'POST':
            platform = request.POST['platform']
            plat = Platform.objects.get(name=platform)
            cour = Course.objects.get(courseid=courseid)
            cour.name = request.POST['name']
            cour.shortdescription = request.POST['shortdescription']
            try:
                description = request.FILES['description']
                cour.description = description
            except:
                pass
            cour.modules = request.POST['modules']
            cour.level = request.POST['level']
            cour.platformid = plat
            cour.save()
            return redirect('course')
        else:
            return redirect('editcourse')
    except:
        return redirect('editcourse')


def deletecourse(request, courseid):
    if 'admin' in request.session:
        cour = Course.objects.get(courseid=courseid)
        cour.delete()
        return redirect('course')
    else:
        return redirect('admin_login')


def lectures(request):
    if 'admin' in request.session:
        lect = Lecture.objects.all()
        return render(request, 'Administrator/tutorialss.html', {'lecture': lect})
    else:
        return redirect('admin_login')


def addlecturepage(request):
    if 'admin' in request.session:
        plat = Platform.objects.all()
        cour = Course.objects.all()
        return render(request, 'Administrator/addlecturepage.html', {'platform': plat, 'course': cour})
    else:
        return redirect('admin_login')



def addlecture(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            video = request.FILES['video']
            course = request.POST['course']
            cour = Course.objects.get(name=course)
            if Lecture.objects.filter(name=name):
                messages.info(request, 'Lecture with same name already exists.')
                return redirect('addlecturepage')
            else:
                lect = Lecture(name=name, description=description, video=video, courseid=cour)
                lect.save()
                return redirect('lectures')
        else:
            return redirect('addlecturepage')
    except:
        return redirect('addlecturepage')


def editlecture(request, lectureid):
    if 'admin' in request.session:
        lect = Lecture.objects.get(lectureid=lectureid)
        plat = Platform.objects.all()
        cour = Course.objects.all()
        return render(request, 'Administrator/editlecture.html', {'lecture': lect, 'platform': plat, 'course': cour})
    else:
        return redirect('admin_login')


def updatelecture(request, lectureid):
    try:
        if request.method == 'POST':
            course = request.POST['course']
            cour = Course.objects.get(name=course)
            lect = Lecture.objects.get(lectureid=lectureid)
            lect.name = request.POST['name']
            lect.description = request.POST['description']
            try:
                lect.video = request.FILES['video']
            except:
                pass
            lect.courseid = cour
            lect.save()
            return redirect('lectures')
        else:
            return redirect('addlecturepage')
    except:
        return redirect('addlecturepage')


def deletelecture(request, lectureid):
    lect = Lecture.objects.get(lectureid=lectureid)
    lect.delete()
    return redirect('lectures')


def questions(request):
    if 'admin' in request.session:
        qa = Qanda.objects.all()
        return render(request, 'Administrator/questions.html', {'qa': qa})
    else:
        return redirect('admin_login')


def addquestionpage(request):
    if 'admin' in request.session:
        lect = Lecture.objects.all()
        cour = Course.objects.all()
        return render(request, 'Administrator/addquestion.html', {'lecture': lect, 'course': cour})
    else:
        return redirect('admin_login')


def addquestion(request):
    try:
        if request.method == 'POST':
            question = request.POST['question']
            lecture = request.POST['lecture']
            course = request.POST['course']
            correct = request.POST['correct']
            optiona = request.POST['optiona']
            optionb = request.POST['optionb']
            optionc = request.POST['optionc']
            lect = Lecture.objects.get(name=lecture)
            cour = Course.objects.get(name=course)
            if Qanda.objects.filter(question=question):
                messages.info(request, 'Question already exists.')
                return redirect('addquestionpage')
            else:
                quest = Qanda(question=question, correct=correct, optiona=optiona, optionb=optionb, optionc=optionc, lectureid=lect, courseid=cour)
                quest.save()
                return redirect('questions')
        else:
            return redirect('addquestionpage')
    except:
        return redirect('addquestionpage')


def editquestionpage(request, qandaid):
    if 'admin' in request.session:
        qa = Qanda.objects.get(qandaid=qandaid)
        lect = Lecture.objects.all()
        cour = Course.objects.all()
        return render(request, 'Administrator/editquestion.html', {'qa': qa, 'lecture': lect, 'course': cour})
    else:
        return redirect('admin_login')


def updatequestion(request, qandaid):
    try:
        if request.method == 'POST':
            qa = Qanda.objects.get(qandaid=qandaid)
            qa.question = request.POST.get('question')
            qa.correct = request.POST.get('correct')
            qa.optiona = request.POST.get('optiona')
            qa.optionb = request.POST.get('optionb')
            qa.optionc = request.POST.get('optionc')
            qa.save()
            return redirect('questions')
        else:
            return redirect('editquestionpage')
    except:
        return redirect('editquestionpage')

def deletequestionanswer(request, qandaid):
    qa = Qanda.objects.get(qandaid=qandaid)
    qa.delete()
    return redirect('questions')


#Jafreena
def usercreate(request):   
        if request.method == 'POST':
            fullname = request.POST['name']
            platformid = request.POST['pid']
            email = request.POST['email']
            cno  = request.POST['cno']
            coid  = request.POST['coid']
            password= request.POST['password']
            conformpassword = request.POST['conformpassword']
            if password == conformpassword:
                if usersign.objects.filter(email=email).exists():
                    messages.info(request, 'This email already exists. Sign up again')
                    return redirect('userreg')
                else:
                    user = usersign.objects.create(fullname=fullname,platformid=platformid, email=email,
                                                    level=0,cno=cno,password=password,score=0, course_id=coid)
                    user.save()
                    return redirect('userlog')
            else:
                messages.info(request, 'Password and conform password does not match')
                return redirect('userreg')
            
def userlog(request):
    return render(request,'user/userlog.html')

def userreg(request):
    pl=Platform.objects.all()  
    c=Course.objects.all()  
    return render(request,'user/userreg.html',{'pl':pl,'c':c})



def gologins(request):    
    return render(request, 'user/user_login.html')

def gosignup(request):  
     return render(request, 'user/user_registration.html')

def userlogin(request):   
        if request.method == 'POST':
            if usersign.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
                l = usersign.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['login']=l.sid
                return redirect('userdash')
                              
            else:
                messages.error(request, 'Invalid Email Id or Password.')
                return render(request, 'user/userlog.html')

def userdash(request):
    l=usersign.objects.get(sid=request.session['login'])
    pl=Platform.objects.get(platformid=l.platformid)
    c=Course.objects.get(courseid=l.course_id)   
    return render(request, 'user/userdash.html',{'pl':pl,'c':c,'l':l})


def userprofile(request):
    l= usersign.objects.get(sid=request.session['login'])
    p= Platform.objects.get(platformid=l.platformid)
    c= Course.objects.get(courseid=l.course_id) 
    return render(request, 'user/profile.html', {'l': l,'p':p,'c':c})

def tutorials(request):
    ll= usersign.objects.get(sid=request.session['login'])
    p= Platform.objects.get(platformid=ll.platformid)
    c= Course.objects.get(courseid=ll.course_id) 
    l= Lecture.objects.filter(courseid=ll.level)
  
   
   
    return render(request, 'user/tutorial.html', {'l': l,'ll':ll,'p':p,'c':c})


     
def tutorialview(request,lectureid):
    try:
        c= Course.objects.get(courseid=request.session['level'])
        l = Lecture.objects.get(lectureid=lectureid,courseid=c)
        p= Platform.objects.get(platformid=request.session['platform'])
        
        

        context = {'l': l, 'c': c,'p':p}
        return render(request, 'user/vidios.html', context)
    except:
        return redirect('tutorials')
def test(request):
    try:
        #u= usersign.objects.get(sid=request.session['login'])
        #s=float(u.score)
        
        #if(s<4):       
        q=list(Qanda.objects.filter(courseid=request.session['level']).order_by('?')[:10])
        random.shuffle(q)
        context = {'q':q}
        return render(request, 'user/test.html', context)
        #else:
         #   return redirect('tutorials')
    except:
        return redirect('tutorials')


def userlogout(request):
    request.session["login"] = ""
    auth.logout(request)
    return redirect('userlog')   

def edituserprofile(request, id):   
    l= usersign.objects.get(sid=id)
    p= Platform.objects.get(platformid=l.platformid)
    c= Course.objects.get(courseid=l.course_id)
    pl=Platform.objects.all()  
    co=Course.objects.all() 
    return render(request,'user/edituserprofile.html',{'l': l,'p':p,'c':c,'pl':pl,'co':co} )

def updateuserprofile(request, id):
        l= usersign.objects.get(sid=id)        
        l.fullname = request.POST['name']
        l.platformid = request.POST['platformid']
        l.email = request.POST['email']
        l.cno  = request.POST['cno']
        l.password = request.POST['password']
        l.save()
        
        return redirect('userlog')
        
def certificate(request):
    l= usersign.objects.get(sid=request.session['login'])
    p= Platform.objects.get(platformid=l.platformid)
    c= Course.objects.get(courseid=l.course_id)
    s=float(l.score)
    if(s>4):
        return render(request,'user/certificate.html',{'l': l,'p':p,'c':c})
    else:        
        return render(request,'user/nocertificate.html',{'l': l,'p':p,'c':c})
def gocertificate(request):
    l= usersign.objects.get(sid=request.session['login'])
    p= Platform.objects.get(platformid=l.platformid)
    c= Course.objects.get(courseid=l.course_id)
    return render(request,'user/certificate.html',{'l': l,'p':p,'c':c})
def gonocertificate(request):
    l= usersign.objects.get(sid=request.session['login'])
    p= Platform.objects.get(platformid=l.platformid)
    c= Course.objects.get(courseid=l.course_id)
    return render(request,'user/nocertificate.html',{'l': l,'p':p,'c':c})




def score1(request):
     if request.method == 'POST':
        l= usersign.objects.get(sid=request.session['login'])
        l.score=request.POST['score']
        l.save()
        u= usersign.objects.get(sid=request.session['login'])
        s=float(u.score)
        if(s>4):
            return redirect('gocertificate')
        else:     
            return redirect('gonocertificate')
