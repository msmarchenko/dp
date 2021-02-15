from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .UserManager import UserManager
# Create your models here.
from keras.models import load_model



class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self


class Composition(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Name: {self.name}"


class Cnn_Model(models.Model):
    # def getModel():
    #     return
    def predict (X):
        model  = load_model('cnn.h5', compile=False)
        return model.predict(X)

class Parameter(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['definition_id', 'name'], name='definition_id_and_parameter_name_constraint')
        ]
    readonly_fields = ('definition_id',)
    TYPE_CHOICES = (
        ('Control', 'Control'),
        ('Quality', 'Quality'),
    )
    name = models.CharField(max_length=50)
    definition_id = models.CharField(max_length=10)#, choices=TYPE_CHOICES, default='Quality')
    position= models.CharField(max_length=50)
#    definition_id = models.IntegerField(blank=True, null=True)
#    position = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Quality')

    def __str__(self):
        return f"Name: {self.name}"


class Machine(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return f"Name: {self.name}"

class Order(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Name: {self.name}"

class KPI(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    werk =  models.ForeignKey(Machine, on_delete=models.CASCADE)
    kd_name = models.CharField(max_length=80, default='None')
    rezeptur = models.CharField(max_length=80)
    material = models.CharField(max_length=80)
    polymer  = models.CharField(max_length=20)
    dicke  = models.FloatField()
    menge  = models.FloatField()
    yields  = models.FloatField()

class Measurements(models.Model):
    date = models.DateTimeField(auto_now_add=False)
    rollenNumber = models.IntegerField()
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    value = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['date'])
        ]

    def __str__(self):
        return f"DateTime: {self.date}, Composition: {self.composition}, Parameter:{self.parameter}"
