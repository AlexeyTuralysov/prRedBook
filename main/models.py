from django.db import models

# Create your models here.


class Population(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    total_count = models.IntegerField()
    male_count = models.IntegerField()
    female_count = models.IntegerField()
    location = models.ForeignKey('Location', related_name='populations', on_delete=models.CASCADE)  # Связь с местоположением

    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name


class Factor(models.Model):
    TYPE_CHOICES = [
        ('Water', 'Water'),
        ('Food', 'Food'),

    ]
    LEVEL_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    STATUS_CHOICES = [
        ('Well', 'Well'),
        ('Normal', 'Normal'),
        ('Bad', 'Bad'),
    ]

    location = models.ForeignKey(Location, related_name='factors', on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    name = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=6, choices=LEVEL_CHOICES)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.type} - {self.name}'


class Threat(models.Model):
    location = models.ForeignKey(Location, related_name='threats', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name