from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')    
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/' , blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
            return self.title 

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"comment by {self.author.username} on {self.post.title}"       
        