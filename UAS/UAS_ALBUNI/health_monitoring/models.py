from django.db import models

class FoodIntake(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='monitoring_food_intakes')
    date = models.DateField()
    food_item = models.CharField(max_length=100)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.food_item} - {self.quantity} on {self.date}"

class Activity(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='monitoring_activities')
    date = models.DateField()
    steps = models.IntegerField()

    def __str__(self):
        return f"{self.steps} steps on {self.date}"
