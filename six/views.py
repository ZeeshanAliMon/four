from django.shortcuts import render,HttpResponse
from six.models import Login
# Create your views here.
def home(request):
    return render(request,"home.html")
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        login =Login(name=name,password=password)
        login.save()
        print(name)
    return render(request,"index.html")