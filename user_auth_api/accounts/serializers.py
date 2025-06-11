from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    birth_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])

    class Meta:
        model = CustomUser
        fields = ('email', 'phone', 'name', 'birth_date', 'gender', 'profile_picture', 'password')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    email_or_phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email_or_phone = data.get("email_or_phone")
        password = data.get("password")
        user = CustomUser.objects.filter(email=email_or_phone).first() or \
               CustomUser.objects.filter(phone=email_or_phone).first()
        if user and user.check_password(password):
            data['user'] = user
            return data
        raise serializers.ValidationError("Invalid credentials")

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'profile_picture', 'email', 'phone', 'birth_date', 'gender')
