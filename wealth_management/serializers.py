from rest_framework import serializers
from wealth_management.models import Bullion, FixedDeposit

class FDSerializer(serializers.ModelSerializer):
    id = str(serializers.PrimaryKeyRelatedField(many=True, read_only=True))
    class Meta:
        model = FixedDeposit
        fields = '__all__'

class BullionSerializer(serializers.ModelSerializer):
    id = str(serializers.PrimaryKeyRelatedField(many=True, read_only=True))
    class Meta:
        model = Bullion
        fields = '__all__'