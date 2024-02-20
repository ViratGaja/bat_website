from django.db import models

# Create your models here.


class Bat(models.Model):
    batname = models.CharField(max_length=20)  # 球盘名称
    email = models.EmailField()
    message = models.TextField(max_length=200)