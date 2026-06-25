from django.shortcuts import render,redirect,HttpResponse
from docapp.api.EmailBackEnd import EmailBackEnd
from django.contrib.auth import  logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from docapp.api.models import CustomUser
from django.shortcuts import render
from docapp.api.models import *
from django.contrib.auth import get_user_model
User = get_user_model()
def BASE(request):
    return render(request,'base.html')


def LOGIN(request):
    return render(request,'login.html')

def doLogout(request):
    logout(request)
    return redirect('login')

def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password')
                                         )
        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                 return redirect('admin_home')
            elif user_type == '2':
                 return redirect('doctor_home')
            elif user_type == '3':
                return HttpResponse("This is User panel")
            
            
        else:
                messages.error(request,'Email or Password is not valid')
                return redirect('login')
    else:
            messages.error(request,'Email or Password is not valid')
            return redirect('login')


login_required(login_url='/')
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    return render(request,'profile.html',context)
@login_required(login_url = '/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        print(profile_pic)
        

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            

            
            if profile_pic !=None and profile_pic != "":
               customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request,"Your profile has been updated successfully")
            return redirect('profile')

        except:
            messages.error(request,"Your profile updation has been failed")
    return render(request, 'profile.html')


def CHANGE_PASSWORD(request):
     context ={}
     ch = User.objects.filter(id = request.user.id)
     
     if len(ch)>0:
            data = User.objects.get(id = request.user.id)
            context["data"]:data            
     if request.method == "POST":        
        current = request.POST["cpwd"]
        new_pas = request.POST['npwd']
        user = User.objects.get(id = request.user.id)
        un = user.username
        check = user.check_password(current)
        if check == True:
          user.set_password(new_pas)
          user.save()
          messages.success(request,'Password Change  Succeesfully!!!')
          user = User.objects.get(username=un)
          login(request,user)
        else:
          messages.success(request,'Current Password wrong!!!')
          return redirect("change_password")
     return render(request,'change-password.html')
def doctor_list(request):
    query = request.GET.get('q')
    if query:
        doctors = Doctor.objects.filter(name__icontains=query) | Doctor.objects.filter(specialization__icontains=query)
    else:
        doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})
def homedoctor(request):
    # Fetching all doctors (You can limit the number for homepage display)
    doctors = Doctor.objects.all()[:6]  # Only fetch top 6 doctors to show on the homepage (optional)

    # Pass doctors to the template
    return render(request, 'index.html', {'doctors': doctors})
def doctor_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        mobno = request.POST['mobno']
        specialization_id = request.POST['specialization_id']
        consultation = request.POST['consultation']
        experience = request.POST['experience']
        location = request.POST['location']
        rating = request.POST['rating']
        profile_pic = request.FILES.get('pic')

        # Save the doctor information
        specialization = Specialization.objects.get(id=specialization_id)
        doctor = Doctor(
            name=f"{first_name} {last_name}",
            specialization=specialization,
            consultation=consultation,
            experience=experience,
            location=location,
            rating=rating,
            profile_image=profile_pic
        )
        doctor.save()

        # Save the doctor registration
        doctor_reg = DoctorReg(
            admin=request.user,
            mobilenumber=mobno,
            doctor=doctor
        )
        doctor_reg.save()

        messages.success(request, "Doctor Registered Successfully.")
        return redirect('doctor_dashboard')

    else:
        specialization = Specialization.objects.all()
        return render(request, 'doctor_registration.html', {'specialization': specialization})