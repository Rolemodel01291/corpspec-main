import requests

from django.conf import settings
from django.contrib import admin
from .models import Activity

from .models import *

def sync_form(modeladmin, request, queryset):
    api = settings.SYNC_URL
    
    auth_req = requests.post(api + 'token/', settings.SYNC_DETAILS)
    token = auth_req.json()['access']

    for obj in queryset:
        form_req = requests.get('%sforms/%s/' % (api, obj.form_id), 
                                headers={'Authorization': 'Bearer %s' % token}
                            )
        obj.form_json = form_req.json()['formly_new']
        obj.save()

@admin.register(Activity)
class Activity(admin.ModelAdmin):
    actions = [sync_form]
