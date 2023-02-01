from django.shortcuts import render
from .models import Posts

# Create your views here.


def index(request):
    posts=Posts.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,dynamic):
    posts=Posts.objects.get(id=dynamic)
    return render(request,'post.html',{'posts':posts})