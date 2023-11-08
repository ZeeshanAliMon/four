from django.db import models

class Login(models.Model):
  name = models.CharField(max_length=120)
  password = models.CharField(max_length=120)
  def __str__(self) :
        return self.name
        
  