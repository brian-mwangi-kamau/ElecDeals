from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("You must provide an email!")
        if not first_name:
            raise ValueError("You must provide your last name!")
        if not last_name:
            raise ValueError("You must provide your last name!")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    

class Gadget(models.Model):
    item_id = models.AutoField(primary_key=True, null=False)
    item_name = models.CharField(max_length=50, null=False)
    item_description = models.TextField(max_length=1000, null=False)
    ITEM_COLOR_CHOICES = [
        ('black', 'Black'),
        ('silver', 'Silver'),
        ('white', 'White'),
        ('space grey', 'Space grey'),
        ('rose gold', 'Rose gold'),
        ('red', 'Red'),
        ('blue', 'Blue')
    ]
    item_color = models.CharField(max_length=50, choices=ITEM_COLOR_CHOICES, null=False)

    ITEM_BRAND_CHOICES = [
        ('apple', 'Apple'),
        ('samsung', 'Samsung'),
        ('dell', 'Dell'),
        ('hp', 'HP'),
        ('lenovo', 'Lenovo'),
        ('acer', 'Acer'),
        ('asus', 'Asus')
    ]
    item_brand = models.CharField(max_length=50, choices=ITEM_BRAND_CHOICES, null=False)

    ITEM_OS_CHOICES = [
        ('windows', 'Windows'),
        ('ios', 'iOS'),
        ('linux', 'Linux'),
        ('macos', 'macOS'),
        ('chromeos', 'ChromeOS'),
        ('android', 'Android'),
        ('harmonyos', 'HarmonyOS')
    ]
    item_os = models.CharField(max_length=50, choices=ITEM_OS_CHOICES, null=False)

    item_type = models.ManyToManyField(
        'Type',
        related_name='gadgets',
        blank=False,
    )

    item_capacity = models.ManyToManyField(
        'Capacity',
        related_name='gadgets',
        blank=True,
    )

    item_features = models.ManyToManyField(
        'Feature',
        related_name='gadgets',
        blank=True,
    )

    item_image = models.ImageField(upload_to='files/', null=False)
    item_price = models.IntegerField(null=False)

    def __str__(self):
        return str(self.item_id) + " " + str(self.item_name)
    

class Type(models.Model):
    type = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.type

class Capacity(models.Model):
    RAM = models.CharField(max_length=50, blank=True)
    ROM = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "capacity"

    def __str__(self):
        return self.RAM + " " + self.ROM
    


class Feature(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
