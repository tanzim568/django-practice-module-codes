from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'navigate/home.html')

def about(request):
    # return render(request,'home.html')
    return render(request,'navigate/about.html')

def contact(request):
    # return render(request,'home.html')
    return render(request,'navigate/contact.html')
