from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    class meta:
        model= Projects
        fields= ['title', 'description', 'category', 'Skill']
    
     # to save the projects 
    def ProjectSave(self, commit=True):
        instance= super().save(commit=False)
        # Manipulate the form data
        instance.title = instance.title.upper()
        instance.description = instance.description.capitalize()
        instance.skill = instance.skill.capitalize()
        
         # Associate the project with a category
        category_id = self.cleaned_data.get('category')
        category = Category.objects.get(id=category_id)
        instance.category = category
        
        # Perform custom validation
        if instance.skill == 'Invalid':
            raise ValidationError('Invalid skill!')
        
        if commit:
            instance.save()
        return instance
        
class ContactForm(forms.ModelForm):
    class meta:
        model=ContactMessage
        fields= ['name', 'email', 'subject', 'message']
     # to save the contacts    
    def contactsave(self, commit=True):
        instance= super().save(commit=False)
        if commit:
            instance.save()
        return instance
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'descriptions', 'category', 'content']
    # to save the blogs
    def blogsave(self, commit=True):
        instance= super().save(commit=False)
        if commit:
            instance.save()
        return instance 