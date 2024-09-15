from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    total_places = models.IntegerField()
    booked_places = models.IntegerField(default=0)
    free_places = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Booking(models.Model):
    user = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

# Create your models here.
