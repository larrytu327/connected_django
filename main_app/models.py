from django.db import models
from django.contrib.auth.models import User

class SchoolClass(models.Model):
    school = models.CharField(max_length=255, default="")
    grade = models.CharField(max_length=20, default="")
    school_type = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.school
    
    class Meta:
        ordering = ['school', 'grade']

class MessageBoard(models.Model):
    name =  models.CharField(max_length=300, default='')
    topics = models.CharField(max_length=300, default='')
    date_added = models.TimeField(auto_now_add=True)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name="messageboard", default="")    
    # posts = models.CharField(max_length=300, default='')    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['topics']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ##on_delete CASCADE, if the profile is deleted, than everything under it gets deleted
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    type  = models.CharField(max_length=255, default='')
    parents = models.CharField(max_length=255, default='')
    students = models.CharField(max_length=255, default='')
    teachers = models.CharField(max_length=255, default='')
    school_class = models.ManyToManyField(SchoolClass)

    def __str__(self):
        return self.first_name
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=750)
    messageboard = models.ForeignKey(MessageBoard, on_delete=models.CASCADE, related_name="post")

    def __str__(self):
        return self.title
    
