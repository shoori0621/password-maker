from django.db import models
from password_maker.models.base import ModelBase
from password_maker.models.user import User
from password_maker.utils.utils import randomChars
from password_maker.services.password_service import encrypt, decrypt
 
import logging

class Account(ModelBase):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False) # 変数名＋_idでカラムが作られる
  name = models.CharField(max_length=255, blank=False, null=True) 
  url = models.TextField(blank=True, null=True)
  password = models.BinaryField(blank=False, null=True)
  salt = models.BinaryField(blank=False, null=True)
  iv = models.BinaryField(blank=False, null=True)
  priority = models.SmallIntegerField(blank=True, null=True)
  memo = models.TextField(blank=True, null=True)

  @property
  def decrypted_password(self):
    return decrypt(self)

  '''
  パスワード生成
  '''
  def generatePassword(self):
    # パスワードを生成(ランダム20文字)
    password_text = randomChars(20)
    data = encrypt(password_text)
    self.password = data['encrypted']
    self.salt = data['salt']
    self.iv = data['iv']

  '''
  パスワード取得
  '''
  def getPassword(self):
    return decrypt(self)

  # モデルが所属するアプリケーションの定義
  class Meta:
    app_label = 'password_maker'
    db_table = 'accounts'
