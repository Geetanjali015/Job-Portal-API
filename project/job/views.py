from django.shortcuts import render,redirect

from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm
from .form import UpdateJobForm
from django.contrib.auth.decorators import login_required
#create a job
@login_required
def create_job(request):
    # Check if the user is authenticated and has the necessary attributes
    if request.user.is_authenticated and hasattr(request.user, 'is_recruiter') and request.user.is_recruiter:
        if hasattr(request.user, 'has_company') and request.user.has_company:
            if request.method == 'POST':
                form = CreateJobForm(request.POST)
                if form.is_valid():
                    var = form.save(commit=False)
                    var.user = request.user
                    var.company = request.user.company
                    var.save()
                    messages.info(request, 'New job has been created')
                    return redirect('dashboard')
                else:
                    messages.warning(request, 'Something went wrong')
                    return redirect('create-job')
            else:
                form = CreateJobForm()
                context = {'form': form}
                return render(request, 'job/create_job.html', context)
        else:
            messages.warning(request, 'You need to have a company to create a job.')
            return redirect('dashboard')
    else:
        messages.warning(request, 'Permission denied. Only recruiters can create jobs.')
        return redirect('dashboard')
   

#update job
def update_job(request,pk):
    job=Job.objects.get(pk=pk)
    if request.method=='POST':
        form=UpdateJobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            messages.info(request,'Your job info has been updated')
            return redirect('dashboard')
        else:
            messages.warning(request,'Something went wrong')
    else:
        form=UpdateJobForm(instance=job)
        context={'form':form}
        return render(request,'job/update_job.html',context)
    
def manage_jobs(request):
    jobs=Job.objects.filter(user=request.user,company=request.user.company)
    context={'jobs':jobs}
    return render(request,'job/manage_jobs.html',context)


def apply_to_job(request,pk):
    if request.user.is_autheticated and request.user.is_applicant:
        job=Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user,job=pk).exists():
            messages.warning(request,'Permission denied')
            return redirect('dashboard')
        else:
            
            ApplyJob.objects.create(
                job=job,
                user=request.user,
                status='Pending'
            )
            messages.info(request,'You have successfully applied! Please see dashboard')
            return redirect('dashboard')
    else:
        messages.info(request,'Please login to continue')
        return redirect('login')
    

def all_applicants(request,pk):
    job=Job.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context={'job':job,'applicants':applicants}
    return render(request,'job/all_applicants.html',context)

def applied_jobs(request):
    jobs=ApplyJob.objects.filter(user=request.user)
    context={'jobs':jobs}
    return render(request,'job/applied_job.html',context)