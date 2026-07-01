from django.db import models

class Hotel(models.Model):
    IdHotel = models.IntegerField(primary_key=True)
    HotelName = models.TextField()
