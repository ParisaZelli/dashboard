from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class post(models.Model):

    domestic='domestic'
    foreign='foreign'

    TYPE_FIELDS=(
        (domestic,'domestic'),(foreign,'foreign')
    )


    title=models.CharField(max_length=255)
    content=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    Active=models.BooleanField(default=False)
    type=models.CharField(max_length=100,default=domestic,choices=TYPE_FIELDS)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    category=models.ManyToManyField("Category")
    image=models.ImageField(null=True,upload_to='blog/',default='blog/OIP_1.jfif')
    tags = TaggableManager()


    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-updated_time']


class description(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE)
    subject=models.CharField(max_length=225,null=True)
    message=models.TextField(blank=True)
    

    def __str__(self):
        return self.subject
    

class Category(models.Model):
    name=models.CharField(max_length=255)


    def __str__(self):
        return self.name
