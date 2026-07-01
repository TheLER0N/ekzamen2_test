from django.db import models

class History(models.Model):
    IdHistory = models.ForeignKey("guest.Guest", on_delete=models.CASCADE)
    GuestId = models.IntegerField(null=True)
    RoomId = models.ForeignKey("room.Room", on_delete=models.CASCADE)
    CheckIn = models.DateField(null=True)
    ChecklnOut = models.DateField(null=True)
    Comment = models.TextField(max_length=200, null=True)

