from django.db import models

# Create your models here.
class Textde(models.Model):
    soz=models.CharField(max_length=100)
    def __str__(self) :
        return f"{self.soz}"
    

class Fintech(models.Model):
    kurs=models.CharField(max_length=100)
    narx=models.IntegerField(default=0)
    mavjudmi=models.BooleanField(default=True)
    def __str__(self) :
        return f"{self.kurs}"