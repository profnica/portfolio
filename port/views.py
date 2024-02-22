from django.shortcuts import render, redirect
from .forms import ProjectForm, ContactForm, SkillForm, BlogPostForm
from .models import Projects, BlogPost, Skills, ContactMessage
from django.conf import settings 
from django.core.mail import send_mail                                                                                                                                                                                                           
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_superuser 

def home(request):
    return render(request, 'port/home.html')

# all functionality involving my skills!!
def skill_list(request):
    skills = Skills.objects.all()
    return render(request, 'port/skill.html', {'skills': skills})

@user_passes_test(is_admin)
def skill_add(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skill_list')
    else:
        form = SkillForm()
    return render(request, 'port/skill_add.html', {'form': form})

@user_passes_test(is_admin)
def skill_delete(request, skill_id):
    skill = Skills.objects.get(id=skill_id)
    if request.method == 'POST':
        skill.delete()
        return redirect('skill_list')
    return render(request, 'port/skill_delete.html', {'skill': skill})

# for all functionailty involving my projects!!
def project(request):
    # Retrieve all projects
    projects = Projects.objects.all()
    return render(request, 'port/project.html', {'projects': projects})

@user_passes_test(is_admin)
def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            # Associate the project with selected skill
            skills = form.cleaned_data['skill']
            # Add a print statement to display the selected skills
            print(f"Selected Skills: {skills}")
            # Assuming Skills.objects.filter(skill__in=skills) returns a list of skill objects
            skills_objs = Skills.objects.filter(skill__in=skills)
            for skill_obj in skills_objs:
                project.skill.add(skill_obj)  # Add each skill object individually
            project.save()
            return redirect('project')
    else:
        form = ProjectForm()
    return render(request, 'port/add_project.html', {'form': form})

@user_passes_test(is_admin)
def project_delete(request, project_id):
    project= Projects.objects.get(id=project_id)
    if request.method =='POST':
        project.delete()
        return redirect('project')
    else:
        return render(request, 'port/delete_project.html', {'project':project})   
    
# for blog post 
def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'port/blog.html', {'blog_posts': blog_posts})

def blog_detail(request, blogpost_id):
    post = get_object_or_404(BlogPost, id=blogpost_id)
    return render(request, 'port/blog_details.html', {'post': post})

@user_passes_test(is_admin)
def blog_add(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = BlogPostForm
    return render(request, 'port/blog_form.html', {'form': form})


@user_passes_test(is_admin)
def blog_delete(request, blogpost_id):
    post = get_object_or_404(BlogPost, id=blogpost_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    return render(request, 'port/blog_delete.html', {'post': post})

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



