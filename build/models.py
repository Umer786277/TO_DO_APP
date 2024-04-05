from django.db import models

# Create your models here.

class User(models.Model):
    

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    def __str__(self):
        return self.name
    