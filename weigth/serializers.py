from rest_framework import serializers

from weigth.models import Weight


class WeigthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = '__all__'
