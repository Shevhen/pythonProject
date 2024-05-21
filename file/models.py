import requests
from django.db import models
from rest_framework.request import Request

class UploadedFile(models.Model):
    id = models.IntegerField(primary_key=int)
    ip = models.CharField(max_length=256)
    file = models.FileField()
    uploaded_on = models.DateTimeField(auto_now_add=True)

    #
    # class Meta:
    #     db_table = 'file_uploadedfile'
    #     app_label = 'file_uploadedfile'
    #
    # def __str__(self):
    #     return self.uploaded_on.date()
