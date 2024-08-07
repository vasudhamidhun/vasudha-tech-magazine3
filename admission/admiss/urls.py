from django.urls import path,include
from .views import *
urlpatterns =[
    path('',index),
    path('login/',loginpage),

    path('clglog/',clglog),
    path('regis/', regis),
    path('success/', success),
    path('send/', send_mail_regis),

    path('error/', error),

    path('verify/<auth_token>', verify),
    path('postcourse/<int:id>',postcourse),
    path('postvacancy/<int:id>',postvacancy),
    path('teacherlog/', teacherlog),
    path('teacherreg/', teacherreg),
    path('editprofile/<int:id>', editprofile),
    path('viewpost/<int:id>', viewjob),
    path('studentlog/', studentlog),
    path('studentreg/', studentreg),
    path('edituser/<int:id>', edituser),
    path('viewcourse/<int:id>', viewcourse),
    path('view/<int:id>/', teacherview),
    path('studentview/<int:id>/', studentview),
    path('applyvac/<int:id1>/<int:id2>', applyvac),
    path('applycourse/<int:id1>/<int:id2>', applycourse),
    path('viewcollege/', viewcollege),
    path('sendmail/<int:id>', sendmail),
    path('viewpro/<int:id>', viewpro),
    path('viewco/<int:id>', viewco),
    path('status/<int:id1>', jobstatus),
    path('viewstatus/<int:id>/', viewstatus),
    path('coursestatus/<int:id1>', coursestatus),
    path('studentstatus/<int:id>/', studentstatus),

]