from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from toDoApp.accounts.serializers import UserSerializer, LoginRequestSerializer, LoginResponseSerializer

UserModel = get_user_model()


class RegisterView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # DEFAULT_PERMISSION_CLASSES in settings.py


@extend_schema(
    tags=['auth'],
    summary='Login endpoint',
    description='Authenticate a user and get back access and refresh tokens',
    request=LoginRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        401: "Invalid username or password",
    }
)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')  # like request.POST in Django not REST
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password,
        )

        if user is None:
            return Response(
                {
                    "error": "Invalid username or password",
                    },
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken().for_user(user)  # returns an object

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful",
                },
            status=status.HTTP_200_OK
        )
