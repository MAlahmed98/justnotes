from django.shortcuts import render
from .models import note
# Create your views here.


def editor(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = note.objects.all()

    content = {
        'noteid': noteid,
        'notes' : notes
    }

    return render(request, 'editor.html', content)


def browse(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = note.objects.all()

    content = {
        'noteid': noteid,
        'notes' : notes
    }
    
    return render(request, 'browse.html', content)

def main(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = note.objects.all()

    content = {
        'noteid': noteid,
        'notes' : notes
    }
    
    return render(request, 'main.html', content)