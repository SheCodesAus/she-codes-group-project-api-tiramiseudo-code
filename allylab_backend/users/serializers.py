from rest_framework import serializers
from .models import CustomUser, PRONOUNS
class CustomUserSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  first_name = serializers.CharField(max_length=30)
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField(write_only=True)
  password = serializers.CharField(max_length=50, write_only=True)
  pronoun = serializers.ChoiceField(choices=PRONOUNS)
  photo = serializers.URLField(allow_blank=True)
  bio = serializers.CharField(max_length=1000)
  
  def create(self, validated_data):
    return CustomUser.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.email = validated_data.get('email', instance.email)
    instance.password = validated_data.get('password', instance.password)
    instance.pronoun = validated_data.get('pronoun', instance.pronoun)
    instance.photo = validated_data.get('photo', instance.photo)
    instance.bio = validated_data.get('bio', instance.bio)
    instance.save
    return instance