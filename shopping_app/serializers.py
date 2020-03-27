from rest_framework import serializers
from shopping_app.models import User_log ,Product

#class UserSerializer(serializers.ModelSerializer):
 #   def create(self, validated_data):
  #      usr_serializer = UserSerializer(validated_data.get('User_log'))
   #     if usr_serializer.is_valid(raise_exception=True):
    #        usr_serializer.save()
     #       return User.objects.create(**validated_data)
    #class Meta:
     #  model = User_log
      # fields = "__all__"

#class Pro_Serializer(serializers.ModelSerializer):
 #  class Meta:
  #     model = Product
   #    fields = "__all__"

class UserSerializerSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=100)
    password=serializers.CharField(max_length=100)

class Item(serializers.Serializer):
    item=serializers.CharField(max_length=200)
    rates=serializers.FloatField()


       