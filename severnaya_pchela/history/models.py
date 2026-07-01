from django.db import models

class History(models.Model):
    IdHistory = models.IntegerField(primary_key=True)
    GuestId = models.ForeignKey("guest.Guest", on_delete=models.CASCADE)
    RoomId = models.ForeignKey("room.Room", on_delete=models.CASCADE)
    CheckIn = models.DateField(null=True)
    ChecklnOut = models.DateField(null=True)
    Comment = models.TextField(max_length=200, null=True)

