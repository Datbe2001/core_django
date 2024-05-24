from core.apps.engine.models import User
from django.contrib.auth.hashers import make_password
from core.apps.engine.serializers_container import (serializers, AppStatus)


class UserRegisterSerializer(serializers.ModelSerializer):
    # referral_code = serializers.CharField(max_length=32, required=False, default="", min_length=0)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, "min_length": 8}}

    def create(self, validated_data):
        user = User.objects.filter(email=validated_data["email"]).first()
        if user and user.is_active:
            raise serializers.ValidationError("Email already exists.")

        password = validated_data.pop('password')
        hashed_password = make_password(password)
        #
        # user = User.objects.create_user(**validated_data)
        # return user
        instance = super().create({**validated_data, 'password': hashed_password})
        return instance


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}, 'verify_code': {'write_only': True}}


class UserDeleteAccountSerializer(serializers.Serializer):
    current_password = serializers.CharField(min_length=8)


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'status_kyc']


class UserLogoutSerializer(serializers.Serializer):
    pass
