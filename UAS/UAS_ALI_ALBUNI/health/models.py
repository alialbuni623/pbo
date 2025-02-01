from django.db import models

class Activity(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    steps = models.IntegerField()
    distance = models.FloatField()
    calories_burned = models.FloatField()

class FoodIntake(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    food_item = models.CharField(max_length=100)
    calories = models.FloatField()
    nutrients = models.JSONField()  # Menyimpan informasi gizi dalam format JSON

class VitalSigns(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateField()
    blood_pressure = models.CharField(max_length=20)
    weight = models.FloatField()
    blood_sugar = models.FloatField()
