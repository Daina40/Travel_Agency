from django.db import models


class DestinationModel(models.Model):
    destination_name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    description = models.TextField()
    img = 

    def __str__(self):
        return self.destination_name
    
class GuideModel(models.Model):
    guide_name = models.CharField(max_length=50)
    expirence = models.CharField(max_length = 50)
    destination = models.ManyToManyField(DestinationModel, related_name='tours')
    person_photo = 
    nid_img = 

    def __str__(self):
        return self.guide_name

    
class TourPackageModel(models.Model):
    title = models.CharField(max_length=50)
    destinations = models.ManyToManyField(DestinationModel, related_name='tours')
    starting_time_date =  models.DateTimeField()
    ending_time_date = models.DateTimeField()
    total_seat = models.PositiveSmallIntegerField()
    seat_booking_number = models.PositiveSmallIntegerField()
    bus_start = models.TimeField()
    type_of_tour = 
    per_person_price = models.PositiveIntegerField()
    img = 

    def __str__(self):
        return self.title
