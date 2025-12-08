from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Speaker, Schedule, Registration
from django.conf import settings

def home(request):
    return render(request, 'website/home.html')

def speakers(request):
    speakers_list = Speaker.objects.all()
    return render(request, 'website/speakers.html', {'speakers': speakers_list})

def schedule(request):
    schedule_list = Schedule.objects.all()
    return render(request, 'website/schedule.html', {'schedule': schedule_list})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        organization = request.POST.get('organization')
        email = request.POST.get('email', 'vnjagi05@gmail.com')
        
        # Save registration
        registration = Registration.objects.create(
            name=name,
            organization=organization,
            email=email
        )
        
        # Send email notification
        try:
            subject = f'New Registration: {name}'
            message = f'Name: {name}\nOrganization: {organization}\nEmail: {email}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['vnjagi05@gmail.com']
            
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Registration successful! You will receive a confirmation email.')
        except Exception as e:
            messages.success(request, 'Registration successful! We\'ll contact you soon.')
        
        return render(request, 'website/register_success.html', {'registration': registration})
    
    return render(request, 'website/register.html')

def payment(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        amount = request.POST.get('amount')
        
        # Here you would integrate with actual payment gateway
        # For now, just show success message
        messages.success(request, f'Payment of KES {amount} initiated for number {number}. You will receive an MPESA prompt.')
        return render(request, 'website/payment_success.html', {'number': number, 'amount': amount})
    
    return render(request, 'website/payment.html')
