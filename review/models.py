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
    

class Post(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=30, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    likes = models.IntegerField(default=0)
    caption = models.TextField(max_length=300)

    @classmethod
    def all_posts(cls) :
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def update_post(cls, id, value):
        cls.objects.filter(id=id).update(image=value)


