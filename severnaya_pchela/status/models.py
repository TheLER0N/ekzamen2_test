from django.db import models

class Status(models.Model):
    IdStatus = models.IntegerField(primary_key=True)
    StatusName = models.TextField(max_length=200, verbose_name="Статус")


