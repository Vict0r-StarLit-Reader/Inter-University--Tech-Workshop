from django.db import models

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=200)
    organization = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    start_time = models.TimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.start_time} - {self.description[:50]}"

class Registration(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=150)
    email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} from {self.organization}"
