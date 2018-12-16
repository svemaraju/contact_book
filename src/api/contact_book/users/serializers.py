from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
        Serialize a User
    """

    token = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=False)

    def get_token(self, obj):
        try:
            token = Token.objects.get(user=obj)
            if token is not None:
                return token.key
        except Exception as e:
            pass
        return Token.objects.create(user=obj).key

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.username = validated_data.get('email')
        user.is_active = True
        user.save()
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if 'password' in validated_data:
            instance.set_password(validated_data.get('password'))
        if 'email' in validated_data:
            instance.username = validated_data.get('email')
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'token']
        extra_kwargs = {'password': {'write_only': True}}


class SigninSerializer(serializers.Serializer):
    """
        Serialize a User for signin
    """

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(email__iexact=attrs['email'])
        if not user.exists():
            raise ParseError(_("Incorrect email or password"))
        elif not user.first().check_password(attrs['password']):
            raise ParseError(_("Incorrect email or password"))
        return attrs