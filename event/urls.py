from django.urls import path

from . import views
urlpatterns = [
   path('', views.home,name="home"),
   path('about/', views.about,name="about"),
   path('hack/', views.hackathon,name="hackathon"),
    path('college/', views.college,name="college"),
    path('news/', views.news,name="news"),
    path('quiz/', views.quizzes,name="quiz"),
    path('workshop/', views.workshop,name="workshop"),
    path('comp/', views.competition,name="comp"),
     path('blog/', views.blog_detail,name="blog"),
    
]