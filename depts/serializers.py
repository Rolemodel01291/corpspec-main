from django.urls import reverse
from django.utils.safestring import mark_safe

from rest_framework import serializers
from .models import *


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'