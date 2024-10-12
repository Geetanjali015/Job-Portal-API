from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume

# register applicants only.
def register_applicant(request):
    if request.method=='POST':
        form =RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_applicant=True
            var.save()
            Resume.objects.create(user=var)
            messages.info(request,'your account has been created')
            return redirect('login')
        else:
            messages.warning(request,'Something went wrong')
            return redirect('register-applicant')
        
    else:
        form=RegisterUserForm()
        context={'form':form}
        return render(request, 'user/register_applicant.html',context)

# register recruiter only.
