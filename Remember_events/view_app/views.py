
from django.shortcuts import render,redirect,get_object_or_404
from scheduleapp.models import Event  
def all_events(request):
    events =Event.objects.all()

    return render(request, 'view_app/all_events.html', {'events': events})


def delete_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('all_events') 