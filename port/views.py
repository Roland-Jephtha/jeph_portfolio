from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.




def index(request):
    skill = Skill.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    project = Project.objects.all()
    resume = Resume.objects.all()
    about = About.objects.all()
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['email']
        message = request.POST['message']
        
        
        contact = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
            
        )
        contact.save()
        messages.success(request, "Message successfully Sent")
    
    
    
    context = {
        'skill': skill,
        'experience': experience,
        'education': education,
        'project': project,
        'resume': resume,
        'about': about,
    }
    return render(request, 'index.html', context)