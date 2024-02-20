from django.shortcuts import render
from .models import Bat

def home(request):
    if request.method == "POST":
        # Use request.POST, not request.post
        username = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Create and save the Bat object
        bat = Bat.objects.create(batname=username, email=email, message=message)
        bat.save()
        
    return render(request, 'index.html')

def sendEmail(request):
    if request.method == 'POST':
        # You might want to validate the form data using Django forms here.

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        template = render_to_string('base/email_template.html', {'name': name, 'email': email, 'message': message})

        subject = request.POST.get('subject', 'Default Subject')  # Provide a default subject if not present

        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['shajaygopi2001@gmail.com']
        )

        email.fail_silently = False
        email.send()

        return render(request,'base/email_sent.html')