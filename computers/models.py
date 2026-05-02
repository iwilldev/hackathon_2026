from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=50)

    # simple string representation 
    def __str__(self):
        return self.room_name

class Computers(models.Model):
    comp_name = models.CharField(max_length=60)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.comp_name