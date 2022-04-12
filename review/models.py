from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_info = models.TextField()
    picture = CloudinaryField('image')
    name = models.CharField(max_length=50)

    def save_profile(self):
        self.save

    def delete_user(self):
        self.delete()
    
    @classmethod
    def edit_profile(cls, id, value):
        cls.objects.filter(id=id).update(profile_name=value)

    def __str__(self):
        return self.user.username