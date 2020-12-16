from django.urls import path

from . import views
urlpatterns = [

    path('login_user/', views.login_u,name="user"),
    path('login_admin/', views.login_a,name="admin"),
    path('register/',views.register,name="register"),
]