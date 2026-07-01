from django.db import models

class RoomType(models.Model):

    IdRoomType = models.IntegerField(primary_key=True)
    RoomTypeId = models.CharField(null=True)