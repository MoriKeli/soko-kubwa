from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class User(AbstractUser):
    id = models.CharField(max_length=25, primary_key=True, editable=False, unique=True)
    first_name = models.CharField(max_length=70, blank=False)
    last_name = models.CharField(max_length=10, blank=False, error_messages='Surname provided is too long!')
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=7, blank=False)
    phone_no = models.CharField(max_length=10, blank=False)
    country = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    national_id = models.CharField(max_length=8, blank=False)
    dob = models.DateField(null=True, blank=False)
    age = models.PositiveIntegerField(default=0, editable=False)
    profile_pic = models.ImageField(upload_to='Users-Dps/', default='default.png')
    is_businessaccount = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.username}'
    
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 400 and img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    class Meta:
        ordering = ['username']
        verbose_name_plural = 'Registered Users'
    