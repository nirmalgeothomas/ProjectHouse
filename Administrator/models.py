from platform import platform
from pydoc import describe
from django.db import models

# Create your models here.
class Userrequestproject(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    projectname = models.CharField(max_length=100)
    projectdescription = models.CharField(max_length=300)
    project_file = models.FileField(upload_to="files/",default='',blank=True)

class Addnewproject(models.Model):
    projectname = models.CharField(max_length=100)
    shortdescription = models.TextField(max_length=300)
    uploadthumbnail = models.ImageField(upload_to='images/', null=True, verbose_name='')
    selectplatform = models.CharField(max_length=100)
    languageused = models.CharField(max_length=100)
    database = models.CharField(max_length=100)
    softwares = models.CharField(max_length=100)
    userinterface = models.CharField(max_length=100)
    projectabstract= models.TextField(max_length=100,default='')
    moduledetails = models.TextField(max_length=100,default='')
    uploadvideo = models.FileField(upload_to='videos/',default='')
    uploadscreenshots = models.ImageField(upload_to='images/', null=True, verbose_name='')
    uploadscreenshots1 = models.ImageField(upload_to='images/', null=True, verbose_name='')
    uploadscreenshots2 = models.ImageField(upload_to='images/', null=True, verbose_name='')
    uploadscreenshots3= models.ImageField(upload_to='images/', null=True, verbose_name='')
    uploadpdf = models.FileField(upload_to='images/', null=True, verbose_name='',default='')
    price= models.CharField(max_length=10, null=True, blank=True, default='')

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'



    @property
    def projectThumb(self):
        try:
            url = self.uploadthumbnail.url

        except:
            url = ''
        return url

    @property
    def uploadscree1(self):
        try:
            url = self.uploadscreenshots.url

        except:
            url = ''
        return url

    @property
    def uploadscree2(self):
        try:
            url = self.uploadscreenshots1.url

        except:
            url = ''
        return url

    @property
    def uploadscree3(self):
        try:
            url = self.uploadscreenshots2.url

        except:
            url = ''
        return url

    @property
    def uploadscree4(self):
        try:
            url = self.uploadscreenshots3.url

        except:
            url = ''
        return url

class Addnewplatform(models.Model):
    platformname = models.CharField(max_length=100)
    uploadthumbnail = models.FileField( upload_to="images/",null=True,blank=True)
    description = models.CharField(max_length=300)
    tutorial_discription = models.CharField(max_length=300)
    tutorial_video = models.FileField(upload_to='videos/', default='')

    @property
    def newplat(self):
        try:
            url = self.uploadthumbnail.url

        except:
            url = ''
        return url

    @property
    def icon(self):
        try:
            url = self.icon.url
        except:
            url = ''
        return url


class profile(models.Model):

    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class meta:
        db_table = "profile"


class GetProject(models.Model):
    project_Detail = models.ForeignKey(Addnewproject, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class add_new_ieee(models.Model):
    selectplatform = models.CharField(max_length=100)
    uploadpdf = models.FileField(upload_to='images/', null=True, verbose_name='')
    title = models.CharField(max_length=100)


class User_req_ieeeproject(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    projectname = models.CharField(max_length=100)
    Location = models.CharField(max_length=300)

class User_req_inbuilt_project(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    projectname = models.CharField(max_length=100)
    Location = models.CharField(max_length=300)

class applyintershipt(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.EmailField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    qualifications= models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    college = models.CharField(max_length=100, default='')


class PhoneOtp(models.Model):
    otp_verify=models.PositiveIntegerField(max_length=6)
    



class Q_A(models.Model):
    platform_name = models.CharField(max_length=200,default='')
    q1 = models.CharField(max_length=300)
    a1 = models.CharField(max_length=300)

class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    platform_name = models.CharField(max_length=200,default='')

    def __str__(self):
        return self.question




class tutorial(models.Model):
    platform_name = models.CharField(max_length=200,default='')
    videotitle = models.CharField(max_length=300)
    uploadvideo = models.FileField(upload_to='videos/', default='')


class Platform(models.Model):
    platformid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="", null=True)
    description = models.CharField(max_length=10000, default="", null=True)


class Course(models.Model):
    courseid = models.AutoField(primary_key=True)
    platformid = models.ForeignKey(Platform, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="", null=True)
    shortdescription = models.CharField(max_length=1000, default="", null=True)
    description = models.FileField(upload_to='files/', default='', null=True)
    modules = models.CharField(max_length=1024, default="", null=True)
    level = models.CharField(max_length=255, default='', null=True)

class Lecture(models.Model):
    lectureid = models.AutoField(primary_key=True)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='', null=True)
    video = models.FileField(upload_to='files/', default='', null=True)
    description = models.CharField(max_length=1024, default='', null=True)

class Qanda(models.Model):
    qandaid = models.AutoField(primary_key=True)
    lectureid = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=255, default='', null=True)
    correct = models.CharField(max_length=255, default='', null=True)
    optiona = models.CharField(max_length=255, default='', null=True)
    optionb = models.CharField(max_length=255, default='', null=True)
    optionc = models.CharField(max_length=255, default='', null=True)

class usersign(models.Model):
    sid = models.AutoField(('SID'), primary_key=True)
    fullname = models.CharField(max_length=100)
    platformid = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cno = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    score=models.FloatField(max_length=100)
    course_id = models.IntegerField(max_length=100)
    

    def __str__(self):
        return self.email + " " + self.password

    class meta:
        db_table = "usersign"
