from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.
def index(request):
    diaries = Entry.objects.all()
    return render(request, 'diary/home.html', {'diary' : diaries})

def add_note(request):
    upload = EntryForm()
    if request.method == 'POST':
        upload = EntryForm(request.POST, request.FILES)
        if upload.is_valid() :
            upload.save()
            print(request.POST)
            return redirect('diary:index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    # else:
    return render(request, 'diary/addNote.html', {'form' : upload})

def delete(request, pk):
    try:
        diaries = Entry.objects.get(id = pk)
    except Entry.DoesNotExist:
        return redirect('diary:index')
    diaries.delete()
    return redirect('diary:index')
    # return render(request, 'diary/home.html', {'diary' : diaries})

def update(request, pk):
    try:
        diaries = Entry.objects.get(id = pk)
    except Entry.DoesNotExist:
        return redirect('diary:index')
    upload = EntryForm(request.POST, instance=diaries)
    if upload.is_valid() :
        upload.save()
        return redirect('diary:index')
    return render(request, 'diary/addNote.html', {'form' : upload})


def notes(request, pk):
    diaries = Entry.objects.get(id = pk)
    return render(request, 'diary/notes.html', {'entry' : diaries})