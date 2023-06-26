from django.urls import path
from . import views

urlpatterns = [
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),
    path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('blog/create/', views.create_blog_post, name='create_blog_post'),
    path('blog/<int:post_id>/edit/', views.edit_blog_post, name='edit_blog_post'),
    path('blog/<int:post_id>/delete/', views.delete_blog_post, name='delete_blog_post'),
    path('blog/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]
