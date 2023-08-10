from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Account
from .forms import AccountEditForm

import logging

class AccountListView(ListView):
    model = Account
    template_name = 'password_maker/index.html'
    context_object_name = 'account_list'
    success_url = '/'

class AccountCreateView(CreateView):
    model = Account
    form_class = AccountEditForm
    template_name = 'password_maker/edit.html'
    success_url = reverse_lazy('password_maker:index')

    def form_valid(self, form):
        # save時に特殊な操作をする
        object = form.save(commit=False)
        # ユーザーを投稿者として保存できるようにする
        #object.user = self.request.user
        object.generatePassword()
        #object.save()
        return super().form_valid(form)

class AccountUpdateView(UpdateView):
    model=Account
    form_class = AccountEditForm
    template_name = 'password_maker/edit.html'
    success_url = reverse_lazy('password_maker:index')
