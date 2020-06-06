from django.db import models

# Create your models here.
from keras.models import load_model

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
        unique_together = (('name', 'definitionid'),)
    TYPE_CHOICES = (
        ('Control', 'Control'),
        ('Quality', 'Quality'),
    )
    name = models.CharField(max_length=50)
    definitionid = models.IntegerField()
    position = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Quality')
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