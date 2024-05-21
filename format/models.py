from django.db import models

# Create your models here.
class FormatModel(models.Model):
    id = models.IntegerField(primary_key=int)
    fromF = models.CharField(max_length=255)
    toF = models.CharField(max_length=255)