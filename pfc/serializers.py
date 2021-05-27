from rest_framework import serializers
from pfc.models import pfc

class pfcSerializer(serializers.ModelSerializer):
    class Meta:
        model = pfc
        fields = [ 'id', 'pfc_name']