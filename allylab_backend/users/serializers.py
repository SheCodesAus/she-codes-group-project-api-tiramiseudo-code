from rest_framework import serializers

# Up to page 3 in Project Setup

class ProjectSerializer(serializers.Serializer):
  first_name = serializers.CharField(max_length=30)
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField(max_length=50)
  password = serializers.CharField(max_length=50)
  pronoun = serializers.CharField(max_length=10)
  photo = serializers.CharField(max_length=200)
  bio = serializers.CharField(max_length=1000)