from typing import Dict, Any
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.apps.engine.utils.exception import HandleExceptionResponse

from core.apps.engine.serializers_container import (serializers, AppStatus)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]):
        # device_token = self.context['request'].data.get('device_token', None)
        data = super().validate(attrs)
        if self.user.soft_delete:
            raise HandleExceptionResponse(AppStatus.ACCOUNT_IS_LOCKED.message, status_code=status.HTTP_400_BAD_REQUEST)
        return data
