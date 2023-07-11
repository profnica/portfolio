from django.db import models


class Category(models.Model):
<<<<<<< HEAD
    CATEGORY_CHOICES = [
        ("WD", "Web development"),
        ("MA", "Mobile Application"),
        ("DA", "Desktop Application"),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
=======
    Category_used= [
    ("WD", "Web development"),
    ("MA", "Mobile Application"),
    ("DA", "Desktop Application"),
]
    category= models.CharField(max_length=3, choices= Category_used)
    
class Skills(models.Model):
    Skill_Used = [
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
    ("PG", "Postgrels"),
    ("MQ", "MySQL"),
    ("RA", "RESTAPI"),
    ("DRF", "Django Rest Framework"),
]
    skill= models.CharField(max_length=3, choices=Skill_Used)    

class Projects(models.Model):
    title= models.CharField(max_length=30)
    description= models.CharField(max_length=250)
    category= models.ForeignKey(Category, on_delete= models.CASCADE)
    skill= models.ForeignKey(Skills, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)
    update= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-update', '-date_added']
>>>>>>> a6bfcf99574e3e5bdb0d9925b8372724f4ec555e
    
    def __str__(self):
        return self.get_category_display()
        

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
    skill = models.CharField(max_length=100, choices=SKILL_CHOICES)
    
    def __str__(self):
        return self.get_skill_display()

class Projects(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    category = models.ManyToManyField(Category)
    skill = models.ManyToManyField(Skills)
    date_added = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-date_added']

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title= models.CharField(max_length=50)
    descriptions= models.CharField(max_length=300)
    content= models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject    
