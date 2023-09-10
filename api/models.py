from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
class ApiUser(AbstractUser):
    ...


class Warhaus(models.Model):
    name = models.CharField(max_length=20)


class Goods(models.Model):
    article = models.CharField(max_length=50)
    warhaus = models.ForeignKey(Warhaus, related_name="goods", on_delete=models.CASCADE)


class Reception(models.Model):
    good = models.ForeignKey(Goods, related_name="receptions", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name="receptions", on_delete=models.CASCADE)
