from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data

        for key, value in serializer.items():
            data[key] = value

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def register(request):
    data = request.data

    username = data["username"]
    email = data["email"]
    phone_number = data["phone_number"]
    password = data["password"]
    password1 = data["password1"]

    if password == password1:
        if User.objects.filter(email=email).exists():
            return Response({"details" : "User with this email is already exists "})
        else:
            if len(password) < 6:
                return Response({"details" : "A strong password contains at least 6 characters "})
            else:
                user = User.objects.create_user(
                    email=email, 
                    username=username, 
                    phone_number=phone_number, 
                    password=password
                )
                user.save()
                return Response({"details" : "New user created successfully "})
    else:
        return Response({'details' : "Passwords do not match "})