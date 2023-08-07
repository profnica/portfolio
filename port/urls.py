from django.urls import path
from . import views

# Update URLs in urls.py
urlpatterns = [
    path('', views.home, name="home"),
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_add, name='skill_add'),
    path('skills/delete/<int:skill_id>/', views.skill_delete, name='skill_delete'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('projects/', views.project, name='project'),
    path('projects/add/', views.project_add, name='project_add'),
    path('projects/delete/<int:project_id>/', views.project_delete, name='project_delete'),
    path('blog/', views.blog, name='blog'),
    path('add/', views.blog_add, name='blog_add'),
    path('delete/<int:blogpost_id>/', views.blog_delete, name='blog_delete'),
    path('post/<int:blogpost_id>/', views.blog_detail, name='blog_detail'),
]


