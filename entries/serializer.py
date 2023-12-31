from rest_framework import serializers
from .models import Entry

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'date', 'purpose', 'time_on_task')
        extra_kwargs = {'purpose': {'required': False}}