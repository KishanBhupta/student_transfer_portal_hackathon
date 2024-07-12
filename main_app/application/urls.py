"""
URL configuration for main_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from application import views
from django.conf.urls.static import static 
from django.conf import settings




urlpatterns = [

    
    path('index/',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('properties/',views.properties,name="properties"),
    path('student_transfer/',views.student_transfer,name="student_transfer"),
    path('services/',views.services,name="services"),


# <--------------------REGISTRATION AND LOGIN(STUDENT)--------------------->

    path('s_login/',views.s_login,name="s_login"),
    path('s_register/',views.s_register,name="s_register"),

# <--------------------REGISTRATION AND LOGIN(COLLEGE)--------------------->

    path('cllgreg/',views.cllgreg,name="cllgreg"),



# <--------------------CRUD FOR TRANSFER_APPLICATION--------------------->

    # path('student_transfer_list/',views.student_transfer_list,name="student_transfer_list"),
    # path('student_transfer_add/',views.student_transfer_add,name="student_transfer_add"),
    path('student_transfer_adddition/',views.student_transfer_adddition,name="student_transfer_adddition"),
    # path('student_transfer_edit/',views.student_transfer_edit,name="student_transfer_edit"),
    # path('student_transfer_update/',views.student_transfer_update,name="student_transfer_update"),
    # path('student_transfer_delete/',views.student_transfer_delete,name="student_transfer_delete"),





# <--------------------CRUD FOR TRANSFER_APPLICATION--------------------->

    path('student_reg_view/',views.student_reg_view,name="student_reg_view"),
    path('student_transfer_list/',views.student_transfer_list,name="student_transfer_list"),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

