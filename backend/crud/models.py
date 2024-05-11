from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    level = models.PositiveIntegerField()
    background = models.CharField(max_length=100)
    alignment = models.CharField(max_length=20)
    experience_points = models.PositiveIntegerField()

class AbilityScore(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    constitution = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    wisdom = models.PositiveIntegerField()
    charisma = models.PositiveIntegerField()

class Skill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    proficiency = models.BooleanField(default=False)
    modifier = models.IntegerField()

class Equipment(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)