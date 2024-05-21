from rest_framework import serializers

from format.models import FormatModel


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormatModel
        fields = ('fromF', 'toF')
