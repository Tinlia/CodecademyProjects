from django.db import models

# The purpose of this file is to practice and review creating and manipulating Models

# Owner Model with a One-To_Many relationship with the Patient Model
class Owner(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)

  # Redefinin the str method
  def __str__(self):
    return self.first_name + " " + self.last_name

# Patient Model with a Many-To_One relationship with the Owner Model
class Patient(models.Model):
  DOG = "DO"
  CAT = "CA"
  BIRD = "BI"
  REPTILE = "RE"
  OTHER = "OT"
  ANIMAL_TYPE_CHOICES = [
    (DOG, "Dog"),
    (CAT, "Cat"),
    (BIRD, "Bird"),
    (REPTILE, "Reptile"),
    (OTHER, "Other"),
  ]
  animal_type = models.CharField(max_length=2, choices=ANIMAL_TYPE_CHOICES, default=OTHER)
  breed = models.CharField(max_length=200)     # Max entry length = 200 chars
  pet_name = models.CharField(max_length=200)  # Max entry length = 200 chars
  age = models.IntegerField(default=0)         # If no entry, default age = 0
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE) # When Owner is deleted, delete this too

  # Formats the string to display the petname then the pet type (i.e., "Captain Whiskers, Cat") 
  def __str__(self):
    return self.pet_name + ", " + self.animal_type

  # Updates the metadata to sort by pet_name
  class Meta:
    ordering = ["pet_name"]


  
