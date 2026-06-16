from django.db import models

# Create your models here.
class Mevalar(models.Model):
    nomi=models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.nomi}"

class Ismlar(models.Model):
    ism=models.CharField(max_length=40)
    def __str__ (self):
        return f"{self.ism}"
