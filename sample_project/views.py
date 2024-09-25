from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is project home page")
    return render(request,'home.html')
    