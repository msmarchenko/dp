from django.db import models

# Create your models here.
class abstractData(models.Model):
    data_id = models.AutoField(primary_key=True)
    type = models.IntegerField()
    data = models.CharField(max_length=150)
    created_at = models.DateField()
    
