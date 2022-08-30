from rest_framework import serializers
from .models import User, PRONOUNS

class UserSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  first_name = serializers.CharField(max_length=30)
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=50)
  pronoun = serializers.ChoiceField(allow_blank=True, choices=PRONOUNS)
  photo = serializers.URLField(allow_blank=True)
  bio = serializers.CharField(max_length=1000)
  # date_created = serializers.DateTimeField()

  def create(self, validated_data):
    return User.objects.create(**validated_data)