from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self,email,username,name,surname,password=None):
        if not email:
            raise ValueError('Este usuario debe tener un correo electronico !')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,email,name,surname,password):
        user = self.create_user(
            email,
            username=username,
            name=name,
            surname=surname,
            password=password
            )
        user.is_admin = True
        user.is_active=True
        user.save()
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=200, blank=False, null=False, unique=True
    )
    email = models.EmailField(verbose_name="Correo Electronico", unique=True)
    name = models.CharField(
        max_length=200, verbose_name="Nombre", blank=True, null=True
    )
    surname = models.CharField(
        max_length=200, verbose_name="Apellido", blank=True, null=True
        )
    creation_date = models.DateTimeField(auto_now=True, verbose_name="Fecha")
    image = models.ImageField(
        verbose_name="Imagen de perfil", upload_to='profile/', blank=True, null=True
        )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    
    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
        
    #ATRIBUTE TO GET THE LOGIN
    USERNAME_FIELD = 'username'
    #FIELDS REQUIRED TO CREATE THE NEW USER
    REQUIRED_FIELDS = ['email', 'name','surname']
    
    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    #is this user admin?
    @property
    def is_staff(self):
        return self.is_admin

    
