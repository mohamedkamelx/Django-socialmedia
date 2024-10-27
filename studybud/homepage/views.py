from django.shortcuts import render
from .models import posts
import datetime
# Create your views here.
def home(request):
    search_input=request.GET.get('coco') or None
    if search_input:
        return render(request,'Ypage.html',{'post':posts.objects.filter(ttext__icontains=search_input)})

    return render(request,'Ypage.html',{'post':posts.objects.all()})


def create(request):
    if request.method=="POST":
        x=request.POST.get("posting")
        data=posts(ttext=x, timee=datetime.datetime.now())
        data.save()
        return render(request,'Ypage.html',{'post':posts.objects.all()})

    return render(request,'posting.html')