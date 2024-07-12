

#Customer side  105 line no

from datetime import date
from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import Http404
from .models import *
from django.db.models import F,DecimalField,Q
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,logout as logout
from django.contrib import messages
from django.http import JsonResponse
# from cart import *



# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def properties(request):
    return render(request,'properties.html')

def student_transfer(request):
    return render(request,'student_transfer.html')

def services(request):
    return render(request,'services.html')




# <--------------------REGISTRATION AND LOGIN--------------------->

# def customerloginsave(request):
#     if request.method == 'POST':
#         Email=request.POST.get('Email')
#         Password1=request.POST.get('Password')
#         Customer1=Customer.objects.filter(c_email_id=Email,c_password=Password1)
#         if Customer1:
#             messages.success(request,"you are successfully login")
#             request.session['c_email_id']=Email
#             return redirect('/home/')
#         else:
#             messages.error(request,"You have Invalid Email or Password")
#             return redirect('/customerlogin/')
#     else:
#         return render(request,'Customerside/customerlogin.html')

# def customerlogin(request):
#         return render(request,'Customerside/customerlogin.html')

# def customerlogout(request):
#         logout(request)
#         messages.error(request,"You have successfully logout")
#         return redirect('/home/')


# def registration(request):
#     Full_Name=request.POST.get('Full_Name')
#     Email=request.POST.get('Email')
#     Password=request.POST.get('Password')
#     password=request.POST.get('password')
#     Number=request.POST.get('Number')


#     #validations 
#     value = {
#     'Full_Name':Full_Name,
#     'Email':Email,
#     'Password':Password,
#     'Number':Number,
#     }
#     error_message = None

#     if(not Full_Name):
#         error_message = "First name is required !!"
#     elif len(Full_Name) < 4:
#         error_message = "Full name must be 4 or more char long"
#     elif not Full_Name.isalnum():
#         error_message = "Full Name should only contain alphabet"
#     elif (not Email):
#         error_message = "Email is required !!"
#     elif len(Email) < 5:
#         error_message = "email must be 5 or more char long"
#     elif (not Number):
#         error_message = "Contact number is required !!"
#     # elif len(Number) <= 10:
#     #     error_message = "Contact number must be 10 digit !!"
#     # elif len(Number) >= 9:
#     #     error_message = "Contact number must be 10 digit !!"
#     elif (not Password):
#         error_message = "Password is required !!"
#     elif Password != password:
#         error_message = " Confirm Password is same as password !!"
#     # elif Customer.isExists():
#     #         error_message = "Email is already Exist !!"  

#     # def isExists(self):
#     #     if Customer.objects.filter(c_email_id = self.Email):
#     #         return True
#     #     return False
    

#     if not error_message:
#         # customer_detail_add.c_password = make_password(Customer.c_password)
#         CUstomer=Customer(c_full_name=Full_Name,c_email_id=Email,
#                                  c_password=Password,c_contact_no=Number) 
#         # customer_detail_add.c_password=make_password(Password.Password)
#         CUstomer.save() 
#         messages.success(request,'You are registred')
#         return redirect('/home/')

#     else:
#         data={ 
#             'error' : error_message,
#             'values' : value,

#         }
#         return render(request,'signup.html',data)



def s_register(request):
    name=request.POST.get('name')
    number=request.POST.get('ph_number')
    gmail=request.POST.get('gmail')
    Password=request.POST.get('password')
    confirm_pass=request.POST.get('confirm_password')

    StudentRegistration=StStudentRegistration(sr_username=name,
                                   sr_call_number=number,
                                   sr_gmail=gmail,
                                  sr_password=Password,sr_confirm_password=confirm_pass) 
    StudentRegistration.save()
    return render(request,'s_register.html')

    #validations 
    # value = {
#     'Full_Name':Full_Name,
#     'Email':Email,
#     'Password':Password,
#     'Number':Number,
#     }
#     error_message = None

#     if(not Full_Name):
#         error_message = "First name is required !!"
#     elif len(Full_Name) < 4:
#         error_message = "Full name must be 4 or more char long"
#     elif not Full_Name.isalnum():
#         error_message = "Full Name should only contain alphabet"
#     elif (not Email):
#         error_message = "Email is required !!"
#     elif len(Email) < 5:
#         error_message = "email must be 5 or more char long"
#     elif (not Number):
#         error_message = "Contact number is required !!"
#     # elif len(Number) <= 10:
#     #     error_message = "Contact number must be 10 digit !!"
#     # elif len(Number) >= 9:
#     #     error_message = "Contact number must be 10 digit !!"
#     elif (not Password):
#         error_message = "Password is required !!"
#     elif Password != password:
#         error_message = " Confirm Password is same as password !!"
#     # elif Customer.isExists():
#     #         error_message = "Email is already Exist !!"  

#     # def isExists(self):
#     #     if Customer.objects.filter(c_email_id = self.Email):
#     #         return True
#     #     return False
    

#     if not error_message:
#         # customer_detail_add.c_password = make_password(Customer.c_password)
#         CUstomer=Customer(c_full_name=Full_Name,c_email_id=Email,
#                                  c_password=Password,c_contact_no=Number) 
#         # customer_detail_add.c_password=make_password(Password.Password)
#         CUstomer.save() 
#         messages.success(request,'You are registred')
#         return redirect('/home/')
    return render(request,'s_register.html')


def s_login(request):
    return render(request,'s_login.html')

# <--------------------CRUD IN STUDENT SIDE--------------------->


def cllgreg(request):
    return render(request,'cllgreg.html')


# <--------------------CRUD IN STUDENT SIDE--------------------->

def student_transfer_adddition(request):
    if request.method == "POST":
        name=request.POST.get('t_s_name')
        gender=request.POST.get('t_gender')
        dob=request.POST.get('t_date')
        community_category=request.POST.get('t_community_category')
        phone_no=request.POST.get('t_phone_number')
        gmail=request.POST.get('t_email')
        address=request.POST.get('t_address')
        present_college=request.POST.get('t_present_college')
        future_college=request.POST.get('t_future_college')
        reason_for_transfer=request.POST.get('t_reason_for_transfer')
        present_course=request.POST.get('Course')
        markslastsem=request.POST.get('markslastsem')
        # aadhar_card=request.POST.get('t_aadhar_card')
        # caste=request.POST.get('t_caste')
        # migration_certi=request.POST.get('t_migration_certificate')
        # last_sem_marks=request.POST.get('markslastsem')

        ac=request.FILES['t_aadhar_card'] 
        fsss=FileSystemStorage()
        file1=fsss.save(ac.name,ac)
        acfile_upload=fsss.url(file1)

        mc=request.FILES['t_migration_certificate'] 
        fsss=FileSystemStorage()
        file3=fsss.save(mc.name,mc)
        mcile_upload=fsss.url(file3)

        caste=request.FILES['t_caste'] 
        fsss=FileSystemStorage()
        file5=fsss.save(caste.name,caste)
        catefole_upload=fsss.url(file5)





        student_transfer1=StTransferForm(t_s_name=name,t_dob=dob,t_gender=gender,t_email=gmail,t_phone_no=phone_no,
                    t_address=address,
                    t_present_college=present_college,
                    t_future_college=future_college,
                    t_reason_for_transfer=reason_for_transfer, 
                    t_present_course=present_course,t_community_category=community_category, t_aadhar_card=acfile_upload, t_caste_certificate=catefole_upload,t_migration_certificate=mcile_upload, t_marks_last_sem=markslastsem)
        student_transfer1.save()
        return redirect('/index/')



# <--------------------CRUD IN ADMIN SIDE--------------------->


def student_reg_view(request):
    student_reg=StStudentRegistration.objects.all()
    return render(request,"admin/student_reg_view.html",{'reg':student_reg})


def student_transfer_list(request):
    student_transfer12=StTransferForm.objects.all()
    return render(request,"admin/student_transfer_list.html",{'st':student_transfer12})