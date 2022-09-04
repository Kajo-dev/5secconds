from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class CastomUserMenago(BaseUserManager):
    def _create_user(self,email,password,first_name,**extra_fields):
        if not email:
            raise ValueError("Email jest wymagany")
        if not password:
            raise ValueError("Hasło jest wymagane")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self,email,password,first_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)

        return self._create_user(email,password,first_name,password,**extra_fields)
    
    def create_superuser(self,email,password,first_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)

        return self._create_user(email,password,first_name,**extra_fields)



class Myuser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(db_index=True,unique=True,max_length=100)
    first_name = models.CharField(max_length=50)

    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CastomUserMenago()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
