from distutils.log import error
from django.shortcuts import render
from django.http import HttpResponse
from .models import customer,customer1
from .forms import customerform,customerform1

from django.core import serializers
url="http://127.0.0.1:8000/"

def index(request):
     form=customerform()
     if request.method=='POST':
                  form=customerform(request.POST)
                  name=request.POST.get('name')
                  address=request.POST.get('address')
                  income=request.POST.get('income')
                  assets=request.POST.get('assets')
                  yearsinbussiness=request.POST.get('yearsinbussiness')
                  customer.objects.create(name=name,address=address,income=income,assets=assets,yearsinbussiness=yearsinbussiness)
                  form.save()
                  return HttpResponse("<h1>Data saved successfully</h1>")

     return render(request,'index.html',{'form':form})
def reg(request):
      #show the data in drop down
       l={'asstes','income','yearsinbussiness'}
       income=customer.objects.filter(income__gt=0).values('income')
       assets=customer.objects.filter(assets__gt=0).values('assets')
       yearsinbussiness=customer.objects.filter(yearsinbussiness__gt=0).values('yearsinbussiness')
           #show the data in drop down
       return render(request,'reg.html',{'l':l,'income':income,'assets':assets,'yearsinbussiness':yearsinbussiness})

     
def login(request):
     form3=customerform1()
     if request.method=='POST':

                    form3=customerform1(request.POST)
                    username=request.POST.get('username')
                    password=request.POST.get('password')
                    l=username
                    if customer1.objects.filter(username=username,password=password).exists():

                               return HttpResponse("<h1>Login Successful </h1>")
                    else:

                                   return HttpResponse("<h1>Login Failed</h1>")
     return render(request,'login.html',{'form3':form3})    
   
     
def signup(request):
     form1=customerform1()
     if request.method=='POST':
                    form1=customerform1(request.POST)
                    username=request.POST.get('username')
                    password=request.POST.get('password')
            

                    customer1.objects.create(username=username,password=password)
                    form1.save()
                    l=useraname
                    return HttpResponse("<h1>Signup Successful {{l}}     </h1>")



     return render(request,'signup.html',{'form1':form1})


              
              
  