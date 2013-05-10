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


class DictKey(models.Model):
    name    = models.CharField(max_length=256)
    
    def __unicode__(self):
        return self.name
    
    
class DictValue(models.Model):
    value   = models.CharField(max_length=256)
    key     = models.ForeignKey(DictKey) 

    def __unicode__(self):
        return self.value
