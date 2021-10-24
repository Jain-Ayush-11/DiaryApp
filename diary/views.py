from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
import os

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
    old_image = Entry.objects.get(id = pk)
    form = EntryForm(request.POST or None, request.FILES or None, instance=old_image)
    if form.is_valid():
        # deleting old uploaded image.
        image_path = old_image.picture.path
        if os.path.exists(image_path):
            os.remove(image_path)

        # the `form.save` will also update your newest image & path.
        form.save()
        return redirect('diary:index')
    return render(request, 'diary/addNote.html', {'form' : form})

def bookmark(request):
    diaries = Entry.objects.all()
    return render(request, 'diary/bookmarks.html', {'diary' : diaries})

def isBookmark(request, pk):
    entry = Entry.objects.filter(id = pk)
    entry.update(isbookmark = True)
    diaries = Entry.objects.all()
    return render(request, 'diary/bookmarks.html', {'diary' : diaries})

def unBookmark(request, pk):
    entry = Entry.objects.filter(id = pk)
    entry.update(isbookmark = False)
    diaries = Entry.objects.all()
    return render(request, 'diary/bookmarks.html', {'diary' : diaries})

def notes(request, pk):
    diaries = Entry.objects.get(id = pk)
    return render(request, 'diary/notes.html', {'entry' : diaries})