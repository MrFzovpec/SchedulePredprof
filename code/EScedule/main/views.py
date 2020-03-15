from django.shortcuts import render, redirect
from .models import Lesson
from datetime import datetime
# Create your views here.
def index(request):
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
    lessons = Lesson.objects.filter(day=day).order_by('time')

    return render(request, 'index/index.html', {'lessons': lessons, 'day': day, 'day_name': days[int(day)]})

def add_lesson_page(request):
    day = request.GET['day']
    return render(request, 'index/add_page.html', {'day': day})

def add_lesson(request):

    check = request.GET.get('lesson_name', None)

    if check:
        new_lesson = Lesson()

        new_lesson.name = request.GET['lesson_name']
        new_lesson.day = request.GET['day']
        new_lesson.time = request.GET['time']
        new_lesson.hometask = request.GET['homework']
        new_lesson.note = request.GET['note']

        new_lesson.save()
    return redirect('/')

def edit_lesson_page(request):
    id = request.GET['id']
    col = request.GET['col']
    current = request.GET['current']
    return render(request, 'index/edit.html', {'col': col, 'id': id, 'current': current})

def edit_lesson(request):
    new_text = request.GET['edited'].replace('\n', '')
    id = request.GET['id']
    col = request.GET['col']
    if col == 'Домашнее задание':
        Lesson.objects.filter(id=id).update(hometask=new_text)
    elif col == 'note':
        Lesson.objects.filter(id=id).update(note=new_text)

    return redirect('/')

def done(request):
    id = request.GET['id']
    Lesson.objects.filter(id=id).update(is_done=True)
    return redirect('/')

def remove(request):
    id = request.GET['id']
    Lesson.objects.filter(id=id).delete()
    return redirect('/')

def edit_inf_page(request):
    id = request.GET['id']
    lesson = Lesson.objects.filter(id=id).get()
    return render(request, 'index/edit_inf.html', {'lesson': lesson})

def edit_inf(request):
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
