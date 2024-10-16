from rest_framework import serializers
from shops.models import *


class Shopserializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=['id','name','latitude','longitude']
