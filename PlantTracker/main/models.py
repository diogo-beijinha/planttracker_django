from django.db import models

# Create your models here.
class Plants(models.Model):
    plant_id = models.AutoField(primary_key=True, editable=False)
    scientific_name = models.CharField(max_length=100, null=False, default="plant")
    common_name = models.CharField(max_length=100, null=False, default="plant")
    image_url = models.CharField(max_length=2000, null=False, default="url")
    add_date = models.DateField(null=False)
    last_watered = models.DateField(null=True)
    water_reminder = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.plant_id}, {self.common_name}"