from django.db.models.expressions import Col
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Collection, Entry
from .forms import EntryForm
from django.views.generic.list import ListView
import os
from django.db.models import Case, Value, When

# Create your views here.
# class Index(ListView):
#     model = Entry
#     template_name = 'home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['diary'] = Entry.objects.all
#         return context


def index(request):
    diaries = Entry.objects.all()
    collection = Collection.objects.all()
    return render(request, 'diary/home.html', {'diary' : diaries , 'collection' : collection})

def viewNote(request, pk):
    diaries = Entry.objects.get(id = pk)
    collection = diaries.collection
    return render(request, 'diary/notes.html', {'entry' : diaries , 'collection' : collection})

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
    entry.update(isbookmark = Case(When(isbookmark=True, then=Value(False)),When(isbookmark=False, then=Value(True))))
    diaries = Entry.objects.all()
    return render(request, 'diary/bookmarks.html', {'diary' : diaries})

def task(request, pk):
    task = Entry.objects.filter(id = pk)
    task.update(completed = Case(When(completed=True, then=Value(False)),When(completed=False, then=Value(True))))
    diaries = Entry.objects.all()
    return redirect('diary:index')

# For Collections Page
def viewCollection(request, pk):
    collection = Collection.objects.get(id = pk)
    notes = Entry.objects.filter(collection = collection)
    return render(request, 'diary/collections.html', {'diary' : notes , 'collection' : collection})
