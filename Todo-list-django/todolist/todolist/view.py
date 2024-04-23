import json
from datetime import datetime
from django.shortcuts import render, redirect

def add_list(request):
    if request=='POST':
        text=request.POST.get('text')
        if text:
            with open('text.json','a') as f:
                note_data={'text':text,'date_created': datetime.now().isoformat()}
                json.dump(note_data,f)
                f.write('\n')

            return redirect('view_list')
    return render(request, 'notes/add_list.html')

def view_list(request):
    notes = []

    with open('text.json', 'r') as f:
        for line in f:
            notes.append(json.loads(line))

    notes.reverse()
    return render(request, 'notes/view_list.html', {'notes': notes})