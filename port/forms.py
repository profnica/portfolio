from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    skill = forms.MultipleChoiceField(
        choices=Skills.SKILL_CHOICES,
        widget=forms.SelectMultiple(attrs={'onclick': 'showOptions(this.nextElementSibling)'}),
    )
    category = forms.MultipleChoiceField(
        choices=Category.CATEGORY_CHOICES,
        widget=forms.SelectMultiple(attrs={'onclick': 'showOptions(this.nextElementSibling)'}),
    )

    class Meta:
        model = Projects
        fields = ['title', 'description', 'skill', 'category', 'link']


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
        fields = ['title', 'descriptions', 'content']
    # to save the blogs
    def blogsave(self, commit=True):
        instance= super().save(commit=False)
        if commit:
            instance.save()
        return instance 