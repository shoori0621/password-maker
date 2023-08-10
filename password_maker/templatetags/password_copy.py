from django import template

register = template.Library()  # Djangoのテンプレートタグライブラリ


# カスタムタグとして登録する
@register.simple_tag
def copy_password(acccount):
    return acccount.getPassword()
