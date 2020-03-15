from django.shortcuts import render, redirect
from .models import Lesson
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        login = request.user.username
        days = {
            1: ' понедельник',
            2: 'о вторник',
            3: ' среда',
            4: ' четверг',
            5: ' пятница',
            6: ' суббота',
            7: ' воскресенье',
        }
        try:
            day = request.GET['day']
        except:
            day = 1
        lessons = Lesson.objects.filter(day=day, user=login).order_by('time')

        return render(request, 'index/index.html', {'lessons': lessons, 'day': day, 'day_name': days[int(day)], 'user': login, 'auf': True})
    else:
        return redirect('/signup')

def add_lesson_page(request):
    if request.user.is_authenticated:
        day = request.GET['day']
        return render(request, 'index/add_page.html', {'day': day})
    else:
        return redirect('/signup')

def add_lesson(request):
    if request.user.is_authenticated:
        login = request.user.username
        check = request.GET.get('lesson_name', None)

        if check:
            new_lesson = Lesson()

            new_lesson.name = request.GET['lesson_name']
            new_lesson.day = request.GET['day']
            new_lesson.time = request.GET['time']
            new_lesson.hometask = request.GET['homework']
            new_lesson.note = request.GET['note']
            new_lesson.user = login

            new_lesson.save()
        return redirect(f'/?day={request.GET["day"]}')
    else:
        return redirect('/signup')

def edit_lesson_page(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        col = request.GET['col']
        current = request.GET['current']
        return render(request, 'index/edit.html', {'col': col, 'id': id, 'current': current})
    else:
        return redirect('/signup')

def edit_lesson(request):
    if request.user.is_authenticated:
        new_text = request.GET['edited'].replace('\n', '')
        id = request.GET['id']
        col = request.GET['col']
        if col == 'Домашнее задание':
            Lesson.objects.filter(id=id).update(hometask=new_text)
        elif col == 'Примечание':
            Lesson.objects.filter(id=id).update(note=new_text)

        return redirect('/')
    else:
        return redirect('/signup')
def done(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        Lesson.objects.filter(id=id).update(is_done=True)
        return redirect('/')
    else:
        return redirect('/signup')

def remove(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        Lesson.objects.filter(id=id).delete()
        return redirect('/')
    else:
        return redirect('/signup')

def edit_inf_page(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        lesson = Lesson.objects.filter(id=id).get()
        return render(request, 'index/edit_inf.html', {'lesson': lesson})
    else:
        return redirect('/signup')

def edit_inf(request):
    if request.user.is_authenticated:
        id = request.GET['id']
        name = request.GET['lesson_name']
        day = request.GET['day']
        hometask = request.GET['homework']
        note = request.GET['note']

        try:
            new_time = request.GET['new_time']
            Lesson.objects.filter(id=id).update(name=name, day=day, hometask=hometask, note=note, time=new_time)
        except:
            Lesson.objects.filter(id=id).update(name=name, day=day, hometask=hometask, note=note)

        return redirect('/')
    else:
        return redirect('/signup')


def login_us(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    else:
        return render(request, 'login/login.html')
def signup(request):
    if request.method == 'POST':
        try:
            User.objects.create_user(username=request.POST['login'], password=request.POST['password'])
        except:
            return redirect('/login')

    return render(request, 'login/register.html', )


def logout_us(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/login')
