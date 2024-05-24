from rest_framework.generics import CreateAPIView
from core.apps.engine.serializers import (
    UserSerializer,
    UserSerializers,
    UserLogoutSerializer,
    UpdateUserSerializer,
    UserRegisterSerializer,
    UserDeleteAccountSerializer,
)
from core.apps.engine.views_container import (
    User, action, openapi, timezone, Response, AppStatus,
    permissions, RefreshToken, GenericAPIView,
    swagger_auto_schema, )


class RegisterViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class VerifyCodeViewSet(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT, properties={
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'verify_code': openapi.Schema(type=openapi.TYPE_STRING)
        },
        required=['email', 'verify_code']),
    )
    def post(self, request):
        email = request.data['email']
        verify_code = request.data['verify_code']
        user = User.objects.filter(email=email).first()
        if user:
            if user.verify_code == verify_code:
                if user.code_lifetime >= timezone.now():
                    user.is_active = True
                    user.save()
                    refresh = RefreshToken.for_user(user)
                    data = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }
                    return Response(data)
                return Response(AppStatus.EXPIRED_VERIFY_CODE.message)
            else:
                return Response(AppStatus.INVALID_VERIFY_CODE.message)
        else:
            return Response(AppStatus.EMAIL_NOT_EXIST.message)


class UserDetailViewSet(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    @action(methods=['get'], url_path='/read_me', detail=False)
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    # @swagger_auto_schema(request_body=openapi.Schema(
    #     type=openapi.TYPE_OBJECT,
    #     properties={
    #         'full_name': openapi.Schema(type=openapi.TYPE_STRING),
    #         'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
    #         'referral': openapi.Schema(type=openapi.TYPE_STRING)
    #     },
    #     required=['full_name', 'phone_number', 'referral']
    # ))
    # @action(methods=['put'], url_path='/update_me', detail=False)
    # def put(self, request, *args, **kwargs):
    #     serializer = UpdateUserSerializer(request.user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         user_me = UserSerializer(request.user)
    #         return Response(user_me.data)
    #     return Response(serializer.errors)


class UserDeleteAccountViewSet(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserDeleteAccountSerializer

    def put(self, request, *args, **kwargs):
        current_user = request.user
        current_password = request.data.get("current_password")

        if current_user.soft_delete:
            return Response(AppStatus.ACCOUNT_HAS_BEEN_DELETED_BEFORE.message)

        if not current_user.check_password(current_password):
            return Response(AppStatus.CURRENT_PASSWORD_INCORRECT.message)

        current_user.soft_delete = True
        current_user.save()
        return Response(AppStatus.DELETE_ACCOUNT_SUCCESS.message)


class UserLogOutViewSet(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def get(self, *args, **kwargs):
        user = self.request.user
        user.device_token = None
        user.save()
        return Response(AppStatus.USER_LOGOUT_SUCCESS.message)
