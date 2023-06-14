from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
STATUS=((0,"Draft"),(1,"Published"))

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Travel', 'Travel'),
        ('Food', 'Food'),
        # Add more category choices as needed
     )
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    #content=models.TextField()
    content=RichTextField(blank=True,null=True)
    status=models.IntegerField(choices=STATUS,default=0)
    thumbnail_url = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES) 
    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title
# Create your models here.
