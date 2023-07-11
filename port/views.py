from django.shortcuts import render, redirect
from .forms import ProjectForm, ContactForm, BlogPostForm, SkillForm
from .models import Projects, BlogPost, Skills, ContactMessage, Category
from django.conf import settings 
from django.core.mail import send_mail                                                                                                                                                                                                           
from django.contrib import messages



def home(request):
    return render(request, 'port/home.html')

# all functionality involving my skills!!
def skill_list(request):
    skills = Skills.objects.all()
    return render(request, 'port/skill.html', {'skills': skills})

def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'port/skill_add.html', {'form': form})

def skill_edit(request, pk):
    skill = Skills.objects.get(id=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'port/skill_edit.html', {'form': form, 'skill': skill})

def skill_delete(request, pk):
    skill = Skills.objects.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'port/skill_delete.html', {'skill': skill})

# for all functionailty involving my projects!!
def project(request):
    # Retrieve all projects
    projects = Projects.objects.all()
    return render(request, 'port/project.html', {'projects': projects})

def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            # Associate the project with selected skills and categories
            skills = form.cleaned_data['skill']
            categories = form.cleaned_data['category']
            project.save()
            project.skill.set(skills)
            project.category.set(categories)
            return redirect('project')
    else:
        form = ProjectForm()
    return render(request, 'port/add_project.html', {'form': form})


def project_edit(request, pk):
    project= Projects.objects.get(id=pk)
    if request.method=='POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
            
    else:
        form = ProjectForm(instance=project)
    return render(request, 'port/edit_project.html', {'form':form, 'project':project})

def project_delete(request, pk):
    project= Projects.objects.get(id=pk)
    if request.method =='POST':
        project.delete()
        return redirect('project')
    else:
        return render(request, 'port/delete_project.html', {'project':project})
    
# for direct contact with me!!
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Save message to database
            contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
            contact_message.save()
            
            # Send email to host email(company email)
            host_subject = 'New contact form submission'
            host_message = f"A new contact form has been submitted by {name} ({email}).\n\nSubject: {subject}\n\nMessage: {message}"
            send_mail(host_subject, host_message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])


            # Retrieve email addresses of all messages in the database
            messages = ContactMessage.objects.all()
            recipient_list = [message.email for message in messages]

            # Send email to recipient(individuals that contact the company)
            recipient_list = [email]
            subject= 'Re Enquiry'
            message = f"Dear {name},\n\nThank you for contacting me. I will get back to you as soon as possible.\n\nBest regards,\n\n\nAdefolalu Adegboyega"
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
            return redirect('success')
    else:
        form = ContactForm()
        return render(request, 'port/contact.html', {'form': form})
        

def contact_success(request):
    return render(request, 'port/contact_success.html')



