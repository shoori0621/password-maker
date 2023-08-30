from django.urls import path

from . import views

app_name = 'password_maker'
urlpatterns = [
    path('', views.AccountListView.as_view(), name='index'),
    path('create', views.AccountCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AccountDeleteView.as_view(), name='delete'),
]
