from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Entry

# diaries = [
#     {'id' : 1, 'title' : 'My Day'},
#     {'id' : 2, 'title' : 'Uhhhh'},
#     {'id' : 1, 'title' : 'Building a django CRUD app'},
# ]

# Create your views here.
def index(request):
    diaries = Entry.objects.all()
    return render(request, 'diary/home.html', {'diary' : diaries})

def add_note(request):
    return render(request, 'diary/addNote.html')

def notes(request, pk):
    diaries = Entry.objects.get(id = pk)
    return render(request, 'diary/notes.html', {'entry' : diaries})