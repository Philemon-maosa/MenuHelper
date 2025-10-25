from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)  # ingredient name
    quantity = models.FloatField(default=0)               # quantity in units
    unit = models.CharField(max_length=50, default='pcs')  # e.g., pcs, grams, liters
    created_at = models.DateTimeField(auto_now_add=True)   # when it was added
    updated_at = models.DateTimeField(auto_now=True)       # last update

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
