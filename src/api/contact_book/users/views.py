from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from contact_book.users.models import User
from contact_book.users.serializers import (
    UserSerializer,
    SigninSerializer,
)


class Register(CreateAPIView):
    """
        Allows a user to register.
    """
    permission_classes = [AllowAny]
    serializer_class = UserSerializer


class SignIn(CreateAPIView):
    """
        Allows a user to sign in
    """
    serializer_class = SigninSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        self.serializer_class(data=self.request.data).is_valid(raise_exception=True)
        user = User.objects.get(email__iexact=self.request.data.get('email'))
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)


class Logout(APIView):
    """
        Allows a user to logout
    """

    def delete(self, request):
        return Response(status=status.HTTP_200_OK)
