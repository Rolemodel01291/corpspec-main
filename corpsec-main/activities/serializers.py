from django.urls import reverse
from django.utils.safestring import mark_safe

from rest_framework import serializers
from .models import *


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class AResSerializer(serializers.ModelSerializer):
    class Meta:
        model = AResponse
        fields = '__all__'
