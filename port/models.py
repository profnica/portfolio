from django.db import models
from datetime import datetime

class Skills(models.Model):
    SKILL_CHOICES = [
        ("DJ", "Django"),
        ("PY", "Python"),
        ("FL", "Flask"),
        ("WB", "Web2py"),
        ("AWS", "AWS"),
        ("HT", "HTML"),
        ("JS", "JavaScript"),
        ("TY", "Typescript"),
        ("JA", "Java"),  
        ("CSS", "CSS"),
        ("DC", "Docker"),
        ("PHP", "PHP"),
        ("SQL", "SQL"),
        ("SQ", "SQLite3"),
        ("PG", "PostgrelSQL"),
        ("MQ", "MySQL"),
        ("RA", "RESTAPI"),
        ("DRF", "Django Rest Framework"),
    ]
    id = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=100, choices=SKILL_CHOICES)
    
    def __str__(self):
        return self.get_skill_display()

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    skill = models.ManyToManyField(Skills)
    link = models.URLField(default='https://github.com/profnica', null=True)
    image= models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=datetime.now, blank=True)
    update = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-update', '-date_added']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    content= models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank= True)
    
    def __str__(self):
        return self.title
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject    
