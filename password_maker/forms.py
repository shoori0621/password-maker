from django import forms

from .models import Account

class AccountEditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'url', 'priority', 'memo')
        labels={
            'name': 'アカウント名',
            'url': 'ログインURL',
            'priority': '優先度（表示）',
            'memo': 'メモ'
        }
        widgets = {
            "url": forms.widgets.TextInput(),
        }
