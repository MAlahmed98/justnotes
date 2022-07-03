from django.shortcuts import render, redirect
from .models import note
# Create your views here.


def editor(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = note.objects.all()
    
    NID = 0
    #in here it's telling me if we requested a form, we do this shit I don't fucking understand 
    if request.method == 'POST':
        NID = int(request.POST.get('noteid', 0)) #in here, he gets the ID of the not, and some other shit
        tit = request.POST.get('title')
        con = request.POST.get('content', '')

        if NID > 0: #if the note ID is not 0
            nott = note.objects.get(pk=NID)
            nott.title = tit
            nott.content = con
            nott.save() #this will insert it into the data base

            return redirect('/?noteid=%i' % NID) 
        else:
            nott = note.objects.create(title=tit, content=con)
            
            return redirect('/?noteid=%i' % nott.id)
    if NID > 0:
        nott = note.objects.get(pk=nott)
    else:
        nott = ''

    content = {
        'noteid': noteid,
        'notes' : notes,
        'note': note
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