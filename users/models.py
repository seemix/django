from django.db import models


# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = 'users'

    name = models.CharField(max_length=20)
    age = models.IntegerField()
