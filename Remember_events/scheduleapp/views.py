
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from .forms import EventForm
from .models import Event
from datetime import datetime
import smtplib


def remember_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['recipient_email']
            scheduled_time = form.cleaned_data['scheduled_time']
            message = form.cleaned_data['message']
            event = Event(
                recipient_email=recipient_email,
                scheduled_time=scheduled_time,
                message=message
            )
            event.save()
            schedule_email(recipient_email, scheduled_time, message)

            
            return HttpResponse('Email scheduled successfully!')
   
    else:
        form = EventForm()
    return render(request, 'scheduleapp/remember_event.html', {'form': form})

# def schedule_email(recipient_email, scheduled_time, message):

    # SMTP server details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'sebikanepal4@gmail.com'
    smtp_password = 'ktjc wcll qywo hxxk'

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # Create email message
    email = EmailMessage()
    email['Subject'] = 'Scheduled Event'
    email['From'] = smtp_username
    email['To'] = recipient_email
    email.set_content(message)

    # Send the email
    server.send_message(email)

    # Quit the SMTP server
    server.quit()


def schedule_email(recipient_email, scheduled_time, message):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'sebikanepal4@gmail.com'
    smtp_password = 'ktjc wcll qywo hxxk'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)


    email_content = f"Subject: Scheduled Event\n From: {smtp_username}\n To: {recipient_email}\n\n\n{message}"


    server.sendmail(smtp_username, recipient_email, email_content)
    server.quit()
