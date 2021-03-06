from django.contrib.auth.models import User
from django.db import models


DEV_MODES = (
    (1, 'inactive'),
    (2, 'active'),
    (3, 'unknown'),
)


class Device(models.Model):
    name   = models.CharField(max_length=256)
    serial = models.CharField(max_length=256)
    mode   = models.IntegerField(choices=DEV_MODES)
    remark = models.TextField()
    owners = models.ManyToManyField(User)
