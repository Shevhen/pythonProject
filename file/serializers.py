from rest_framework import serializers
from file.models import UploadedFile

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:

        model = UploadedFile
        fields = ('file', 'uploaded_on', 'ip', 'path',)

    # def find(self, model):
    #     UploadedFile.