from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager


# TextChoices
class GencerChoice(models.TextChoices):
    MALE = 'M', _('Masculino')
    FEMALE = 'F', _('Feminino')


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)


class UserMain(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', unique=True, max_length=11)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cpf']

    def __str__(self):
        return self.email

    objects = UserManager()


class UserProfile(models.Model):

    user = models.OneToOneField(
        UserMain, 
        verbose_name=_("Usuário"), 
        on_delete=models.CASCADE,
        )
    
    gender = models.CharField(_("Sexo"), max_length=1, choices=GencerChoice.choices)
    birth_date = models.DateField(_("Data de Nascimento"))

    class Meta:
        verbose_name = 'Perfil do Usuário'
        verbose_name_plural = 'Perfils dos Usuários'

    def __str__(self):
        return self.user.get_full_name()