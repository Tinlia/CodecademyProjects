from django.db import models
import datetime

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00
# Schema:
  # Bike
    # bike_type (standar, tandem, electric)
    # colour (colour of the bike)
  # Renter
    # first_name (of the renter)(text/char)
    # last_name (of the renter)(text/char)
    # phone (number of the renter)(text/char)
    # vip_num (vip number of renter)(integer)
  # Rental
    # bike (what bike is being rented)(FKey)
    # renter (who's renting the bike)(FKey)
    # date (the date of the rental)(datetime)
    # price (of the rental)(integer)


# Bike Model
class Bike(models.Model):
  STANDARD = "ST"
  TANDEM = "TA"
  ELECTRIC = "EL"

  BIKE_TYPE_CHOICES = [
    (STANDARD, "Standard"),
    (TANDEM, "Tandem"),
    (ELECTRIC, "Electric")
  ]
  bike_type = models.CharField(max_length=2, choices=BIKE_TYPE_CHOICES, default=STANDARD)
  color = models.CharField(max_length=10, default="")

  def __str__(self):
    return self.bike_type + " - " + self.color

# Renter Model
class Renter(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=15)
  vip_num = models.IntegerField(default=0)
  def __str__(self):
    return self.first_name + " " + self.last_name + " - #" + self.phone

# Rental Model
class Rental(models.Model):
  bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
  renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
  date = models.DateField(default=datetime.date.today)
  price = models.FloatField(default=0.0)

  def calc_price(self):
    curr_price = BASE_PRICE
    if self.bike.bike_type == "TA":
      curr_price += TANDEM_SURCHARGE
    if self.bike.bike_type == "EL":
      curr_price += ELECTRIC_SURCHARGE
    if self.renter.vip_num > 0:
      curr.price *= 0.8
    self.price = curr_price
