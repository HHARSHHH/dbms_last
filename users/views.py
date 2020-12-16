from django.shortcuts import render

# Create your views here.

def login_u(request):
    return render(request,'login_user.html')

def login_a(request):
    return render(request,'login_admin.html')
def register(request):
    return render(request , 'register.html')