from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken



class UserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ["id", "email", "username", "phone_number"]

    def get_username(self, obj):
        return obj.username
    
    def get_id(self,obj):
        return obj.id

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ["id", "email", "username", "phone_number", "token"]

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)