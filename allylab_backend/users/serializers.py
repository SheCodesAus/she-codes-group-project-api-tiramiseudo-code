from rest_framework import serializers
from .models import CustomUser, PRONOUNS, Skill

class CustomUserSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  first_name = serializers.CharField(max_length=30)
  last_name = serializers.CharField(max_length=50)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=50, write_only=True)
  pronoun = serializers.CharField(source='get_pronoun_display')
  photo = serializers.URLField(allow_blank=True)
  bio = serializers.CharField(max_length=1000)
  skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects, many=True)

  def update(self, instance, validated_data):
    instance.first_name = validated_data.get('first_name', instance.first_name)
    instance.last_name = validated_data.get('last_name', instance.last_name)
    instance.email = validated_data.get('email', instance.email)
    instance.password = validated_data.get('password', instance.password)
    instance.pronoun = validated_data.get('pronoun', instance.pronoun)
    instance.photo = validated_data.get('photo', instance.photo)
    instance.bio = validated_data.get('bio', instance.bio)
    instance.skill = validated_data.get('skills', instance.skill)
    instance.save
    return instance

  def create(self, validated_data):
    skills = validated_data.pop('skills')
    password = validated_data.pop('password')
    print(password)
    user = CustomUser.objects.create(**validated_data)
    user.set_password(password)
    print(user.password)
    user.skills.set(skills)
    user.save()
    return user



    # def to_internal_value(self, data):
    #     # To support inserts with the value
    #     if data == '' and self.allow_blank:
    #         return ''
    #     for key, val in self._choices.items():
    #         if val == data:
    #             return key
    #     self.fail('invalid_choice', input=data)


class SkillSerializer(serializers.ModelSerializer):
  users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
      model = Skill
      fields = ('id', 'skill_name', 'icon', 'users')

  def create(self, validated_data):
    return Skill.objects.create(**validated_data)


class CustomUserDetailSerializer(serializers.ModelSerializer):
  skills = SkillSerializer(many=True, read_only=True)
  
  class Meta:
    model = CustomUser
    fields =( "id", "first_name", "last_name", "pronoun", "photo","bio", "skills")

