from django import forms
from .models import Skills, Projects, BlogPost, ContactMessage
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError


class ProjectForm(forms.ModelForm):
    skill = forms.MultipleChoiceField(
        choices=Skills.SKILL_CHOICES)

    class Meta:
        model = Projects
        fields = ['title', 'description', 'skill', 'link', 'image']
        widgets= {
            'skill': forms.SelectMultiple,
            'image': forms.ClearableFileInput(attrs={'multiple':True}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content'] 
        widgets = {
            'content': CKEditorWidget(),
        }
        
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