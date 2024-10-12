from django.shortcuts import render,redirect

def proxy(request):
    if request.user.is_applicant:
        return redirect('applicant-dashboard')
    elif request.user.is_recruiter:
        return redirect('recruiter-dashboard')
    else:
        return redirect('login')
    

def applicant_dashboard(request):
    return render('dashboard/applicant_dashboard.html')

def recruiter_dashboard(request):
    return render('dashboard/recruiter_dashboard.html')



