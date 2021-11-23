from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from djoser.conf import settings
from rest_framework import serializers
from .models import UserProfile, Buttons, AccidentsType,Accidents
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

"""
формат полей дат yyyy-mm-dd hh-mm-ss
"""
User = get_user_model()

class ButtonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buttons
        fields = "__all__"

    def create(self, validated_data):
        return Buttons.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Number = validated_data.get('Post',instance.Number)
        instance.save()
        return instance



class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = "__all__"

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user',instance.user)
        instance.Role = validated_data.get('Role',instance.Role)
        instance.AccesList = validated_data.get('AccesList',instance.AccesList)
        instance.save()
        return instance



class ButtonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buttons
        fields = "__all__"
    
    def update(self, instance, validated_data):
        instance.TimeStamp = validated_data.get('TimeStamp', instance.TimeStamp)
        instance.save()
        return instance


class AccidentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accidents
        fields = "__all__"

    def create(self, validated_data):
        return Accidents.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Post = validated_data.get('Post', instance.Post)
        instance.Description = validated_data.get('Description',instance.Description)
        instance.FixTime = validated_data.get('FixTime',instance.FixTime)
        instance.EndTime = validated_data.get('EndTime',instance.EndTime)
        instance.save()
        return instance



class AccidentsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentsType
        fields = "__all__"

    def create(self, validated_data):
        return AccidentsType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.TypeName = validated_data.get('TypeName',instance.TypeName)
        instance.save()
        return instance



class ChangeTypeOfUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'is_staff', 'is_superuser', 'date_joined')
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.save()
        return instance



class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
    }

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            settings.USER_ID_FIELD,
            "password",
            "is_staff",
            "is_superuser",
        )

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        instance.save()
        return instance


class ChangeTypeOfMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'is_staff', 'date_joined')
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance

