from django.db import models


class DestinationModel(models.Model):
    destination_name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    description = models.TextField()
    img = models.ImageField(upload_to = 'media/DestinationImages')

    def __str__(self):
        return self.destination_name
    
class GuideModel(models.Model):
    guide_name = models.CharField(max_length=50)
    expirence = models.CharField(max_length = 50)
    destination = models.ManyToManyField(DestinationModel, related_name='tours')
    person_photo = models.ImageField(upload_to = 'media/GuidePhoto')
    nid_frontside_img = models.ImageField(upload_to = 'media/NIDImages')
    nid_backside_img = models.ImageField(upload_to = 'media/NIDImages')

    def __str__(self):
        return self.guide_name

    
class TourPackageModel(models.Model):
    title = models.CharField(max_length=50)
    guide = models.ForeignKey("GuideModel", on_delete = models.CASCADE)
    starting_time_date =  models.DateTimeField()
    ending_time_date = models.DateTimeField()
    total_seat = models.PositiveSmallIntegerField()
    seat_booking_number = models.PositiveSmallIntegerField()
    bus_start = models.TimeField()
    type_of_tour = (
        ('Hajj', 'Hajj tour'),
        ('Couple', 'Couple tour'),
        ('Institute', 'Institute tour'),
        ('Business', 'Business tour'),
        ('Single', 'Single tour'),
    )
    tour_field = models.CharField(max_length=15, choices=type_of_tour)
    per_person_price = models.PositiveIntegerField()
    thumbnail_img = models.ImageField(upload_to = 'media/ThumbnailImages')

    def __str__(self):
        return self.title
