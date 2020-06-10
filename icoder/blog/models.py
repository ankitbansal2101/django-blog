from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    content=models.CharField(max_length=500)
    slug=models.CharField(max_length=50)
    

    def __str__(self):
        return self.title  

class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parent=models.ForeignKey("self",on_delete=models.CASCADE,null=True)
    timestamp=models.DateField(default=now)