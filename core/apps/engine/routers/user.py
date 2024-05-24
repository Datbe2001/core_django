from core.apps.engine.routers import *

from core.apps.engine.views import (
    RegisterViewSet, VerifyCodeViewSet, UserDeleteAccountViewSet,
    UserDetailViewSet, UserLogOutViewSet
)

urlpatterns = [
    path('auth/register/', RegisterViewSet.as_view(), name='register'),
    path('auth/verify-code/', VerifyCodeViewSet.as_view(), name='verify'),

    path('user/me/', UserDetailViewSet.as_view(), name='user-detail'),
    path('user/logout/', UserLogOutViewSet.as_view(), name='user-logout'),
    path('user/delete-account/', UserDeleteAccountViewSet.as_view(), name='user-delete-account'),
]
