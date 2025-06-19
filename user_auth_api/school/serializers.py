from rest_framework import serializers
from .models import SchoolLocation
from accounts.models import CustomUser

class JoinSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolLocation
        fields = ('lat', 'lon')

    def create(self, validated_data):
        user = self.context['request'].user
        return SchoolLocation.objects.create(user=user, **validated_data)

class SchoolLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolLocation
        fields = ('lat', 'lon', 'joined_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'phone', 'profile_picture')
