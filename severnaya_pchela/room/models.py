from django.db import models

class Room(models.Model):
    IdRoom = models.IntegerField(primary_key=True)
    Number = models.IntegerField(null=True)
    RooomTypeId = models.ForeignKey("roomType.RoomType",on_delete=models.CASCADE)
    HotelId = models.ForeignKey("hotel.Hotel",on_delete=models.CASCADE)


    def __str__(self):
        return str(self.IdRoom)