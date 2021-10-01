from django.db import models

# Create your models here.
class Superheroes(models.Model):
    superhero_name = models.CharField(max_length=50)
    alter_ego_name = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)

    def __str__(self):
        return self.superhero_name
    
    
