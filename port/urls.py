from django.urls import path
from . import views

# Update URLs in urls.py
urlpatterns = [
    path('', views.home, name="home"),
    path('skills/', views.skill_list, name='skill_list'),
    path('skills/add/', views.skill_add, name='skill_add'),
    path('skills/edit/<int:pk>/', views.skill_edit, name='skill_edit'),
    path('skills/delete/<int:pk>/', views.skill_delete, name='skill_delete'),
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('projects/', views.project, name='project'),
    path('projects/add/', views.project_add, name='project_add'),
    path('projects/edit/<int:pk>/', views.project_edit, name='project_edit'),
    path('projects/delete/<int:pk>/', views.project_delete, name='project_delete'),
]


