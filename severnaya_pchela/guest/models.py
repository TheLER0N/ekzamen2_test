from django.db import models

class Guest(models.Model):
    idGuest = models.IntegerField(primary_key=True)
    FullName = models.TextField(verbose_name="Полное имя")
    Email = models.EmailField()
    Birthday = models.DateField(verbose_name="День рождение")
    GenderId = models.ForeignKey("gender.Gender", on_delete=models.CASCADE, verbose_name= "пол")
    StatusId = models.ForeignKey("status.Status", on_delete=models.CASCADE, verbose_name="Статус")

    def __str__(self):
        return f"{self.FullName} {self.Birthday}"


