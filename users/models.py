from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
