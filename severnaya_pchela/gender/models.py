from django.db import models

class Gender(models.Model):
    IdGender = models.AutoField(primary_key=True)
    GenderName = models.CharField(max_length = 100)

def __str__(self):
        return f"{self.GenderName}"