from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"home.html")

def count(request):
    data = request.GET["Area"]
    list_ed = data.split()
    len_ = len(list_ed)
    di ={}
    for k in list_ed:
        if k in di:
            di[k]+=1
        else:
            di[k]=1
    
    return render(request,"count.html",{"text":data,"count":len_,"dict":di.items()})

def about(request):
    return render(request,"about.html")