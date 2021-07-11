import shortuuid

from django.contrib.postgres.fields import JSONField
from django.db import models

from depts.models import Department

# Create your models here.
class Activity(models.Model):
    uuid = models.CharField('Uuid', max_length=50, blank=True, null=True)
    name = models.CharField('Activity Name', max_length=200)
    form_id  = models.IntegerField()
    form_json = JSONField(blank=True, null=True)
    document = models.FileField(blank=True, null=True)
    doc_conf = JSONField(blank=True, null=True)
    schedule = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = shortuuid.uuid()
        super().save(*args, **kwargs)


class AResponse(models.Model):
    uuid = models.CharField('Uuid', max_length=50, default='')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    data = JSONField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.uuid = shortuuid.uuid()
        super().save(*args, **kwargs)