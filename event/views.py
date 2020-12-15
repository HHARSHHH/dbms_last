from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def login_u(request):
    return render(request,'login_user.html')

def login_a(request):
    return render(request,'login_admin.html')


def hackathon(request):
    return render(request,'hackathon.html')

def college(request):
    return render(request,'college.html')

def competition(request):
    return render(request,'competition.html')

def news(request):
    return render(request,'news.html')

def quizzes(request):
    return render(request,'quizzes.html')

def workshop(request):
    return render(request,'workshop.html')


def blog_detail(request):
    return render(request,'blog-single.html')