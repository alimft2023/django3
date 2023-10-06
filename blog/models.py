from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.body + ' ' + str(self.id)
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField()
    is_validate=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.created_at