from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description', 'category', 'skill']
        widgets = {
            'skill': forms.SelectMultiple(attrs={'onclick': 'this.size=15;', 'onblur': 'this.size=0;'}),
            'category': forms.SelectMultiple(attrs={'onclick': 'this.size=15;', 'onblur': 'this.size=0;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the choices for skill and category fields
        self.fields['skill'].choices = Skills.SKILL_CHOICES
        self.fields['category'].choices = Category.CATEGORY_CHOICES


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

        
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