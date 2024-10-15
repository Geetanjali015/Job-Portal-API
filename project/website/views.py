from django.shortcuts import render
from job.models import Job

def home(request):
    return render(request,'website/home.html')


def job_listing(request):
    jobs=Job.objects.filter(is_available=True)
    context={'jobs':jobs}
    return render(request,'website/job_listing.html',context)

def job_details(request,pk):
    job=Job.objects.get(pk=pk)
    context={'job':job}
    return render(request,'website/job_details.html',context)
