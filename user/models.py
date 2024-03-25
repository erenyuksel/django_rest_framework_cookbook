import random
from django.db import models
from django.contrib.auth.models import User
def code_generator(length=5):
  numbers = '0123456789'
  return "".join(random.choice(numbers) for _ in range(length))

class UserRegister(models.Model):
    code = models.CharField(max_length=5, default=code_generator)
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
