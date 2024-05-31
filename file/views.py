from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from file.file_changer import FileChanger
from file.models import UploadedFile
from file.serializers import FileUploadSerializer

import requests
from django.core.files import File
from django.http import HttpResponse
from configs.settings import BASE_DIR, MEDIA_ROOT
import os

from concurrent.futures import ThreadPoolExecutor
from spire.doc import *
import pypandoc


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    def post(self, *args, **kwargs):

        data = {
            'file': self.request.data.get('file'),
            'ip': self.request.META.get('REMOTE_ADDR'),
            'path': './dir',
        }
        serializer = FileUploadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, *args, **kwargs):
        form = self.request.query_params.get('f')
        ip = self.request.META.get('REMOTE_ADDR')
        FileChanger(form, ip)

        return Response('done!')

    def delete(self, *args, **kwargs):
        ip = self.request.META.get('REMOTE_ADDR')
        file = UploadedFile.objects.get(ip=ip)
        os.remove(file.new_file.__str__())
        os.remove(file.path + '/' + file.file.__str__())
        file.delete()
        return Response('done!')


class FileDownloader(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    def get(self, *args, **kwargs):
        ip = self.request.META.get('REMOTE_ADDR')
        file = UploadedFile.objects.get(ip=ip)
        path_to_file = file.new_file.__str__()
        f = open(path_to_file, 'rb')
        pdfFile = File(f).read()
        # print(pdfFile)
        response = HttpResponse(pdfFile)
        response['Content-Disposition'] = 'attachment'
        return response