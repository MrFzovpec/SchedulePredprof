from django.shortcuts import render, redirect
from .models import Lesson
# Create your views here.
def index(request):
    try:
        day = request.GET['day']
    except:
        day = 1
    lessons = Lesson.objects.filter(day=day)
    return render(request, 'index/index.html', {'lessons': lessons, 'day': day})

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
