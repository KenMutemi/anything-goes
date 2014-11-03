from rest_framework import serializers
from main.models import Summary

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('id', 'title', 'url', 'fetch_date')
