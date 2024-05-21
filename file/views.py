from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from file.models import UploadedFile
from file.serializers import FileUploadSerializer

import requests
from django.core.files import File
from django.http import HttpResponse
from configs.settings import BASE_DIR, MEDIA_ROOT
import os

from format.format_changer import FormatChanger
from concurrent.futures import ThreadPoolExecutor

class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer

    def post(self, *args, **kwargs):
        data = {
            'file': self.request.data.get('file'),
            'ip': self.request.META.get('REMOTE_ADDR')
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            # print()
            # os.mkdir(os.path.join('../dir', serializer.data.get('ip')))

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def get(self, *args, **kwargs):
        f = self.request.GET.get('f')
        ip = self.request.META.get('REMOTE_ADDR')
        file = UploadedFile.objects.get(ip=ip)
        new_name = file.file.__str__().split('.')[0] + '.pdf'
        # with open(file.file.__str__(), 'r') as fileg: text = fileg.read()
        # with open(new_name, 'w') as fileg: fileg.write(text)

        FormatChanger(file, new_name, f)
        return Response('file here!')

    def download(self):
        path_to_file = MEDIA_ROOT + '/NOTICE.pdf'
        f = open(path_to_file, 'rb')
        pdfFile = File(f).read()
        # print(pdfFile)
        response = HttpResponse(pdfFile)
        response['Content-Disposition'] = 'attachment'
        return response

