"""EScedule URL Configuration

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
from django.urls import path
from main.views import index, add_lesson, add_lesson_page, edit_lesson_page, edit_lesson, done, remove, edit_inf_page, edit_inf, login_us, signup, logout_us

urlpatterns = [
    path('', index),
    path('add_lesson/', add_lesson),
    path('admin/', admin.site.urls),
    path('add_lesson_page/', add_lesson_page),
    path('edit_lesson_page/', edit_lesson_page),
    path('edit_lesson/', edit_lesson),
    path('done/', done),
    path('remove/', remove),
    path('edit/', edit_inf_page),
    path('edit_inf/', edit_inf),
    path('login/', login_us),
    path('signup/', signup),
    path('logout/', logout_us)
]
