from django.shortcuts import render, redirect
from .forms import ProjectForm, ContactForm, BlogPostForm
from .models import Projects, BlogPost

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            # Optionally perform additional actions after saving the project
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

def edit_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            # Optionally perform additional actions after saving the project
            return redirect('project_detail', project_id=project.id)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'edit_project.html', {'form': form, 'project': project})

def delete_project(request, project_id):
    project = Projects.objects.get(id=project_id)
    if request.method == 'POST':
        project.delete()
        # Optionally perform additional actions after deleting the project
        return redirect('projects_list')
    return render(request, 'delete_project.html', {'project': project})

def project_detail(request, project_id):
    project = Projects.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project': project})

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            # Optionally perform additional actions after saving the blog post
            return redirect('blog_post_detail', post_id=blog_post.id)
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

def edit_blog_post(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            # Optionally perform additional actions after saving the blog post
            return redirect('blog_post_detail', post_id=blog_post.id)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'edit_blog_post.html', {'form': form, 'blog_post': blog_post})

def delete_blog_post(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)
    if request.method == 'POST':
        blog_post.delete()
        # Optionally perform additional actions after deleting the blog post
        return redirect('blog_posts_list')
    return render(request, 'delete_blog_post.html', {'blog_post': blog_post})

def blog_post_detail(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog_post_detail.html', {'blog_post': blog_post})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally perform additional actions after saving the contact message
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')



