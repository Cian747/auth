from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50,blank=True,null=True)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    personal_email = models.EmailField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    # @classmethod
    # def update_profile_photo(cls, id,family_email):
    #     return cls.objects.filter(id = id).update(family_email=family_email)

    
    # @classmethod
    # def search_username(cls,search_term):
    #     return cls.objects.filter(user__username__icontains = search_term)

    # def get_absolute_url(self):
    #     return reverse('profile',args=[str(self.id)])

