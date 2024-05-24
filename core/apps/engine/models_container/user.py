from core.apps.engine.models_container import (UserManager, make_password, AbstractBaseUser,
                                                       PermissionsMixin, models, uuid)
from core.apps.engine.models_container.enum_type import SystemRoleEnum
from core.apps.engine.utils.utils import generate_code_by_domain


# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.referral = generate_code_by_domain()
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        extra_fields.setdefault('referral', generate_code_by_domain())
        extra_fields.setdefault('role', SystemRoleEnum.SUPER_ADMIN)

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('role', SystemRoleEnum.USER)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    password = models.CharField(max_length=128, blank=True)
    full_name = models.CharField(max_length=128, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    referral = models.CharField(max_length=30, null=True,  blank=True)
    pre_referral = models.CharField(max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=False, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    verify_code = models.CharField(max_length=10, blank=True)
    password_2fa = models.CharField(max_length=256, null=True, blank=True)
    role = models.CharField(max_length=30, null=False, blank=False, choices=SystemRoleEnum.choices(),
                            default=SystemRoleEnum.USER)
    address_wallet = models.CharField(max_length=128, null=True, blank=True)
    password_wallet = models.CharField(max_length=128, null=True, blank=True)
    soft_delete = models.BooleanField(default=False, blank=True)
    objects = CustomUserManager()
