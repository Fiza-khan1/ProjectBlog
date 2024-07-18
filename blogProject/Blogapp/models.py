from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class PostModel(models.Model):
    title=models.CharField( max_length=50)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateField(auto_now_add=True)
    class Meta:
     ordering = ('-date_created',)

    def __str__(self):
        return self.title    
    def comment_count(self):
       return self.comments_set.all().count()
    

class comments(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   post=models.ForeignKey(PostModel,on_delete=models.CASCADE)
   content=models.CharField(max_length=100)
   parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
   created_on = models.DateTimeField(auto_now_add=True)
   def __str__(self):
        return self.user.username
