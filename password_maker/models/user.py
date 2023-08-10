from django.db import models
from password_maker.models.base import ModelBase

class User(ModelBase):
  last_name = models.CharField(max_length=255, blank=False, null=True)
  first_name = models.CharField(max_length=255, blank=False, null=True)
  email = models.TextField(blank=False, null=True)
  password = models.TextField(blank=False, null=True)

  class Meta:
    app_label = 'password_maker'
    db_table = 'users'