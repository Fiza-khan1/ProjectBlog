from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg'])], default='default.PNG')
    def __str__(self):
        return self.user.username