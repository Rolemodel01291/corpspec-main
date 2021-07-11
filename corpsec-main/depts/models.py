from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from clients.models import Client

class Department(MPTTModel):
    uuid = models.CharField('Uuid', max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    incorp = models.DateField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']