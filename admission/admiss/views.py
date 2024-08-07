from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *

from .forms import *
from admission.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
import uuid
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")
def loginpage(request):
    return render(request,"loginpage.html")

def clglog(request):

    global User;
    if request.method=='POST':
        username=request.POST.get('uname')
        pas=request.POST.get('password')
        user_obj =User.objects.filter(username=username).first()   #vasudha vasu---->Usermodel---->usernm,pas,email===userobj
        if user_obj is None:
            messages.success(request, 'college not found')
            return redirect(clglog)
        profile_obj=profile1.objects.filter(user=user_obj).first()   #user--->userobj===profileobj-----user,isvarifi,authtoken,createdat
        if not profile_obj.is_verified:

            messages.success(request,'profile not verified check ur email')
            return redirect(clglog)
        user = authenticate(username=username, password=pas)

        if user is None:
            messages.success(request,'wrong password or username')
            return redirect(clglog)
        obj=profile1.objects.filter(user=user)
        return render(request,'collegehome.html',{'obj':obj})
    return render(request,'collegelogin.html')


def verify(request,auth_token):
    profile_obj=profile1.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account already verified')
            redirect(clglog)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'ur account verified')
        return redirect(clglog)

    else:
        return redirect(error)

def error(request):
    return render(request,'error.html')


# User--->username email passwrod first_name last_name
def regis(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pas=request.POST.get('password')

        if User.objects.filter(username=uname).first():
            messages.success(request,"username already taken")
            return redirect(regis)

        if User.objects.filter(email=email).first():
            messages.success(request, "email already taken")
            return redirect(regis)

        user_obj=User(username=uname,email=email)
        user_obj.set_password(pas)
        user_obj.save()

        auth_token=str(uuid.uuid4())
        profile_obj=profile1.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return redirect(success)
    return render(request,"collegereg.html")


def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f'pass the link to verify your account http://127.0.0.1:8000/verify/{token}'
    # message='pass the link to verify your account http://127.0.0.1:8000/verify/{}'.format(token)
    # message = 'pass the link to verify your account http://127.0.0.1:8000/verify/'+token

    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def success(request):
        return render(request, "success.html")


def postcourse(request,id):
    userid=id
    user = profile1.objects.get(id=userid)

    if request.method=='POST':
        a = postcourseform(request.POST)
        if a.is_valid():
            name = a.cleaned_data['uname']
            eml = a.cleaned_data['email']
            c=a.cleaned_data['course']
            s= a.cleaned_data['spec']
            d = a.cleaned_data['duration']
            m=a.cleaned_data['mode']
            f = a.cleaned_data['fee']
            e = a.cleaned_data['eligibility']
            ads = a.cleaned_data['address']
            p = a.cleaned_data['phone']

            b = postcoursemodel(uname=name,email=eml,course=c,spec=s,duration=d,mode=m,fee=f,eligibility=e,address=ads,phone=p,id=userid)
            b.save()
            return HttpResponse("sucess..")
        else:
            return HttpResponse("failed")
    return render(request,'postcourse.html',{'user':user})



def postvacancy(request,id):
    userid=id
    user = profile1.objects.get(id=userid)

    if request.method=='POST':


            name = request.POST.get("uname")
            eml = request.POST.get("email")
            j = request.POST.get("jobtitle")
            wt = request.POST.get("wrktype")
            ex =request.POST.get("exp")
            jt = request.POST.get("jobtype")
            sa = request.POST.get("salary")
            e = request.POST.get("eligibility")
            ads = request.POST.get("address")
            p = request.POST.get("phone")

            b = postvacmodel(uname=name,email=eml,jobtitle=j,wrktype=wt,exp=ex,jobtype=jt,salary=sa,eligibility=e,address=ads,phone=p,id=userid)
            b.save()
            return HttpResponse("sucess..")

    return render(request,'postvacancy.html',{'user':user})


def teacherlog(request):
    if request.method=="POST":
        a=teacherlogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            pas = a.cleaned_data['pas']
            b = teacherregmodel.objects.all()#  same as select * from tablename retrieve all details in table
            for i in b:

                if em==i.email and pas==i.password:
                    unm=i.uname
                    eml=i.email
                    ph=i.phone
                    ql=i.qualification
                    id1=i.id

                    return render(request,'teacherhome.html',{'unm':unm,'eml':eml,'ph':ph,'ql':ql,'id':id1})

                    # return HttpResponse("login success....")


            else:
                return HttpResponse("email and password incorrect....")


        else:
            return HttpResponse("enter valid data...")

    return render(request,'teacherlogin.html')


def  teacherreg(request):
    if request.method=='POST':
        a=teacherregform(request.POST)
        if a.is_valid():

            unm=a.cleaned_data['uname']
            eml=a.cleaned_data['email']
            db=a.cleaned_data['dob']
            phn=a.cleaned_data['phone']
            qm=a.cleaned_data['qualification']
            pas=a.cleaned_data['password']
            cpas=a.cleaned_data['cpassword']
            if pas==cpas:
                b=teacherregmodel(dob=db,phone=phn,qualification=qm,uname=unm,email=eml,password=pas)
                b.save()
                return HttpResponse("sucessfully registered")
               # return redirect(log)
            else:
                return HttpResponse("password and cpassword is not match")
        else:
             return HttpResponse("Enter a valid data")
    return render(request,'teacherreg.html')


def editprofile(request,id):
    user = teacherregmodel.objects.get(id=id)
    if request.method=='POST':
        user.uname=request.POST.get('uname')
        user.email=request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.qualification = request.POST.get('qualification')
        user.save()
        return redirect(teacherlog)
    return render(request, 'editprofile.html', {'user': user})

def viewjob(request,id):
    userid=id

    user=teacherregmodel.objects.get(id=userid)
    job=postvacmodel.objects.all()

    id=[]
    uname=[]
    email=[]
    jobtitle=[]
    wrktype=[]
    exp=[]
    jobtype=[]
    salary = []
    eligibility = []
    address = []
    phone=[]

    for i in job:
        un=i.uname
        uname.append(un)
        em=i.email
        email.append(em)
        jt=i.jobtitle
        jobtitle.append(jt)
        wt=i.wrktype
        wrktype.append(wt)
        e=i.exp
        exp.append(e)
        j=i.jobtype
        jobtype.append(j)
        s = i.salary
        salary.append(s)
        el = i.eligibility
        eligibility.append(el)
        ads = i.address
        address.append(ads)
        ph = i.phone
        phone.append(ph)

        idno=i.id
        id.append(idno)
    mylist=zip(uname,email,jobtitle,wrktype,exp,jobtype,salary,eligibility,address,phone,id)
    return render(request,'viewjob.html',{'mylist':mylist,'user':userid})
def studentlog(request):
    if request.method=="POST":
        a=studentlogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            pas = a.cleaned_data['pas']
            b = studentregmodel.objects.all()#  same as select * from tablename retrieve all details in table
            for i in b:

                if em==i.email and pas==i.password:
                    unm=i.uname
                    eml=i.email
                    ph=i.phnno
                    ql=i.qualification
                    id1=i.id

                    return render(request,'studenthome.html',{'unm':unm,'eml':eml,'ph':ph,'ql':ql,'id':id1})

                    # return HttpResponse("login success....")


            else:
                return HttpResponse("email and password incorrect....")


        else:
            return HttpResponse("enter valid data...")

    return render(request,'studentlogin.html')


def  studentreg(request):
    if request.method=='POST':
        a=studentregform(request.POST)
        if a.is_valid():

            unm=a.cleaned_data['uname']
            eml=a.cleaned_data['email']
            db=a.cleaned_data['dob']
            phnno=a.cleaned_data['phnno']
            qm=a.cleaned_data['qualification']
            pas=a.cleaned_data['password']
            cpas=a.cleaned_data['cpassword']
            if pas==cpas:
                b=studentregmodel(dob=db,phnno=phnno,qualification=qm,uname=unm,email=eml,password=pas)
                b.save()
                return HttpResponse("sucessfully registered")
               # return redirect(log)
            else:
                return HttpResponse("password and cpassword is not match")
        else:
             return HttpResponse("Enter a valid data")
    return render(request,'studentreg.html')



def edituser(request,id):
    user = studentregmodel.objects.get(id=id)
    if request.method=='POST':
        user.uname=request.POST.get('uname')
        user.email=request.POST.get('email')
        user.phnno = request.POST.get('phnno')
        user.qualification = request.POST.get('qualification')
        user.save()
        return redirect(studentlog)
    return render(request, 'edituser.html', {'user': user})


def viewcourse(request,id):
    userid=id

    user=studentregmodel.objects.get(id=userid)
    job=postcoursemodel.objects.all()

    id=[]
    uname=[]
    email=[]
    course=[]
    spec=[]
    duration=[]
    mode=[]
    fee = []
    eligibility = []
    address = []
    phone=[]

    for i in job:
        un=i.uname
        uname.append(un)
        em=i.email
        email.append(em)
        c=i.course
        course.append(c)
        sp=i.spec
        spec.append(sp)
        d=i.duration
        duration.append(d)
        m=i.mode
        mode.append(m)
        f = i.fee
        fee.append(f)
        el = i.eligibility
        eligibility.append(el)
        ads = i.address
        address.append(ads)
        ph = i.phone
        phone.append(ph)

        idno=i.id
        id.append(idno)
    mylist=zip(uname,email,course,spec,duration,mode,fee,eligibility,address,phone,id)
    return render(request,'viewcourse.html',{'mylist':mylist,'user':userid})




def applyvac(request,id1,id2):

    job = postvacmodel.objects.get(id=id1)

    user= teacherregmodel.objects.get(id=id2)
    if request.method=='POST':

            cname = request.POST.get("cname")
            j=request.POST.get("jobtitle")
            eml=request.POST.get("email")
            uname=request.POST.get("uname")
            ex=request.POST.get("exp")
            q=request.POST.get("quali")
            p=request.POST.get("phone")
            r=request.POST.get("resume")
            b = applyvacmodel(cname=cname, jobtitle=j,uname=uname,email=eml,phone=p,exp=ex,quali=q,resume=r)
            b.save()
            return HttpResponse("sucess..")

    return render(request,'vacancyapply.html',{'user':user,'job':job})




def applycourse(request,id1,id2):

    job = postcoursemodel.objects.get(id=id1)

    user= studentregmodel.objects.get(id=id2)
    if request.method=='POST':
        # a = courseform(request.POST,request.FILES)
        # if a.is_valid():

            cname = request.POST.get("cname")
            c=request.POST.get("course")
            s = request.POST.get("spec")

            eml=request.POST.get("email")
            uname=request.POST.get("uname")
            d=request.POST.get("dob")
            q=request.POST.get("quali")
            p=request.POST.get("phone")
            ce=request.POST.get("certi")
            b = applycoursemodel(cname=cname,course=c,spec=s,uname=uname,email=eml,dob=d,phone=p,quali=q,certi=ce)
            b.save()
            return HttpResponse("sucess..")

    return render(request,'applycourse.html',{'user':user,'job':job})




def viewcollege(request):

    u = profile1.objects.all()
    id=[]
    username = []
    email = []
    for i in u:
        un = i.user.username
        username.append(un)
        em = i.user.email
        email.append(em)
        id1=i.id
        id.append(id1)

    mylist = zip(username, email,id)
    return render(request, 'viewcollege.html', {'mylist': mylist})


def sendmail(request,id):

    user=profile1.objects.get(id=id)
    if request.method == "POST":
        sub = mailform(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['email']
            name = sub.cleaned_data['name']
            msg = sub.cleaned_data['message']
            send_mail((str(name)) + '||' + str(email), msg, EMAIL_HOST_USER, [email], fail_silently=False)
            # subject+fromemail+recipientemail+message

            return render(request, 'mailsuccess.html')
    return render(request, 'sendmail.html', {'user':user})


def viewpro(request,id):
    u=teacherregmodel.objects.get(id=id)
    user_name=u.uname
    data=applyvacmodel.objects.all()
    cn=[]
    job=[]

    for i in data:
        if i.uname==user_name:
            cn1=i.cname
            cn.append(cn1)
            jtitle1=i.jobtitle
            job.append(jtitle1)

    list=zip(cn,job)
    return render(request,"viewpro.html",{'list':list})


def viewco(request,id):
    u=studentregmodel.objects.get(id=id)
    user_name=u.uname
    data=applycoursemodel.objects.all()
    cn=[]
    job=[]
    spe=[]

    for i in data:
        if i.uname==user_name:
            cn1=i.cname
            cn.append(cn1)
            jtitle1=i.course
            job.append(jtitle1)
            s1=i.spec
            spe.append(s1)

    list=zip(cn,job,spe)
    return render(request,"viewco.html",{'list':list})

def teacherview(request,id):
    com=profile1.objects.get(id=id)
    co_name=com.user.username
    data=applyvacmodel.objects.all()
    id=[]
    job=[]
    nm=[]
    eml=[]
    q=[]
    ph=[]
    exp=[]
    cv=[]
    for i in data:
        if i.cname==co_name:
            jtitle1=i.jobtitle
            job.append(jtitle1)
            name1=i.uname
            nm.append(name1)
            email1=i.email
            eml.append(email1)
            quali1=i.quali
            q.append(quali1)
            ph1=i.phone
            ph.append(ph1)
            ex1=i.exp
            exp.append(ex1)
            res=i.resume
            cv.append(str(res).split('/')[-1])
            id1=i.id
            id.append(id1)

    list=zip(job,nm,eml,q,ph,exp,cv,id)
    return  render(request,"teacherappview.html",{'list':list})
def jobstatus(request,id1):

    job = applyvacmodel.objects.get(id=id1)
    if request.method=='POST':


            name = request.POST.get("uname")
            eml = request.POST.get("email")
            j = request.POST.get("jobtitle")
            ph = request.POST.get("phone")
            ex =request.POST.get("exp")
            qua = request.POST.get("quali")
            apre = request.POST.get("apprej")
            re = request.POST.get("reason")



            b = apprejmodel(uname=name,email=eml,jobtitle=j,quali=qua,exp=ex,apprej=apre,reason=re,phone=ph,id=id1)
            b.save()
            return HttpResponse("sucess..")

    return render(request,'approvereject.html',{'job':job})

def viewstatus(request,id):
    u=applyvacmodel.objects.get(id=id)
    user_name=u.uname
    data=apprejmodel.objects.all()
    un=[]
    eml=[]
    jt=[]
    qua=[]
    ex=[]
    appre=[]
    re=[]
    ph=[]


    for i in data:
        if i.uname==user_name:
            cn1=i.uname
            un.append(cn1)
            e1=i.email
            eml.append(e1)
            j1=i.jobtitle
            jt.append(j1)
            q1=i.quali
            qua.append(q1)
            ex1=i.exp
            ex.append(ex1)
            app1=i.apprej
            appre.append(app1)
            p1=i.phone
            ph.append(p1)
            re1 = i.reason
            re.append(re1)


    list=zip(un,eml,jt,appre,re,ph)
    return render(request,"viewstatus.html",{'list':list})

def studentview(request,id):
    com=profile1.objects.get(id=id)
    co_name=com.user.username
    data=applycoursemodel.objects.all()
    id=[]

    cour=[]
    speci=[]
    nm=[]
    eml=[]
    q=[]
    ph=[]
    db=[]
    cert=[]
    for i in data:
        if i.cname==co_name:
            jtitle1=i.course
            cour.append(jtitle1)
            sp1 = i.spec
            speci.append(sp1)
            name1=i.uname
            nm.append(name1)
            email1=i.email
            eml.append(email1)
            quali1=i.quali
            q.append(quali1)
            ph1=i.phone
            ph.append(ph1)
            ex1=i.dob
            db.append(ex1)
            cer=i.certi
            cert.append(str(cer).split('/')[-1])
            id1 = i.id
            id.append(id1)

    list=zip(nm,eml,cour,speci,q,db,ph,cert,id)
    return  render(request,"studentappview.html",{'list':list})



def coursestatus(request,id1):

    job = applycoursemodel.objects.get(id=id1)
    if request.method=='POST':


            name = request.POST.get("uname")
            eml = request.POST.get("email")
            c = request.POST.get("course")
            ph = request.POST.get("phone")
            spe =request.POST.get("spec")
            qua = request.POST.get("quali")
            apre = request.POST.get("apprej")
            re = request.POST.get("reason")



            b = studentapprejmodel(uname=name,email=eml,course=c,quali=qua,spec=spe,apprej=apre,reason=re,phone=ph,id=id1)
            b.save()
            return HttpResponse("sucess..")

    return render(request,'courseapprej.html',{'job':job})

def studentstatus(request,id):
    u=applycoursemodel.objects.get(id=id)
    user_name=u.uname
    data=studentapprejmodel.objects.all()
    un=[]
    eml=[]
    c=[]
    qua=[]
    spe=[]
    appre=[]
    re=[]
    ph=[]


    for i in data:
        if i.uname==user_name:
            cn1=i.uname
            un.append(cn1)
            e1=i.email
            eml.append(e1)
            j1=i.course
            c.append(j1)
            q1=i.quali
            qua.append(q1)
            ex1=i.spec
            spe.append(ex1)
            app1=i.apprej
            appre.append(app1)
            p1=i.phone
            ph.append(p1)
            re1 = i.reason
            re.append(re1)


    list=zip(un,eml,c,spe,appre,re,ph)
    return render(request,"studentstatus.html",{'list':list})

