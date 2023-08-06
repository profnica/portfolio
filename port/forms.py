from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    skill = forms.MultipleChoiceField(
        choices=Skills.SKILL_CHOICES)
    category = forms.MultipleChoiceField(
        choices=Category.CATEGORY_CHOICES)

    class Meta:
        model = Projects
        fields = ['title', 'description', 'skill', 'category', 'link']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
 
        
class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields= ['name', 'email', 'subject', 'message']
     # to save the contacts    
    def contactsave(self, commit=True):
        instance= super().save(commit=False)
        if commit:
            instance.save()
        return instance