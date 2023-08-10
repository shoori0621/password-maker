from django.db import models

class ModelBase(models.Model):
  class Meta:
      # マイグレーション時にテーブルを作成しないModelは以下のオプションが必要
      abstract = True

  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)