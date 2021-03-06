"""AFexam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views
from user import views as user_views
from examiner import views as examiner_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'), 
    path('profile/',user_views.profile,name='profile'),  
    path('',views.home,name='home'),
    path('panel/',views.panel, name='panel'),
    path('student_home/',include('student.urls')),
    path('examiner_home/',include('examiner.urls')),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('portfolio/',views.portfolio, name='portfolio'),
    path('contact/',views.contact, name='contact'),
    
    

    

] 
