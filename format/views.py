from rest_framework.response import Response
from rest_framework.views import APIView

from format.models import FormatModel
from format.serializer import FormatSerializer


# Create your views here.
class FormatView(APIView):
    class_serializer = FormatSerializer

    def get(self, *args, **kwargs):
        FormatModel.objects.all()
        # queryset = FormatModel.objects.all()
        serializer = FormatSerializer(FormatModel.objects.filter(), many=True)

        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = self.class_serializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data
            )
        return Response(
            serializer.errors
        )