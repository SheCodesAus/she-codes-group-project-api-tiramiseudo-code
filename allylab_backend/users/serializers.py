from rest_framework import serializers
from .models import User, Skill, PRONOUNS

class UserSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  first_name = serializers.CharField(max_length=30)
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=50)
  pronoun = serializers.ChoiceField(allow_blank=True, choices=PRONOUNS)
  photo = serializers.URLField(allow_blank=True)
  bio = serializers.CharField(max_length=1000)
  skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects, many=True)

  def create(self, validated_data):
    skills = validated_data.pop('skills')
    user = User.objects.create(**validated_data)
    user.skills.set(skills)
    return user

class SkillSerializer(serializers.ModelSerializer):
  users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
      model = Skill
      fields = ('id', 'skill_name', 'icon', 'users')

  def create(self, validated_data):
    return Skill.objects.create(**validated_data)
