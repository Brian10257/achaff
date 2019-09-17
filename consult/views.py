from django.shortcuts import render, redirect 
from django.contrib import messages
from django.core.mail import send_mail
from .models import Consult

def consult(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        consult = Consult(name=name, email=email, phone=phone, message=message)
        consult.save()

        # Send Mail
        send_mail(
            'Consulting Inquiry',
            'There has been a Consultation request from WolvesGate Real Estate, Contact the administrator for more info',
            'ntschangb@gmail.com', 
            ['onlinefabico@gmail.com', 'ntschangb@gmail.com'],
            fail_silently=False
        )

        messages.success(request, ' Your request has been submitted, a Consultant will get back to you soon')
        return redirect('consult')

    return render(request, 'consult/consult.html')