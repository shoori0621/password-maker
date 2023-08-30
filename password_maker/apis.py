from rest_framework import viewsets, routers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Account
from django.shortcuts import get_object_or_404

class AccountViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['get'])
    def decrept_password(self, request, pk=None):
        if pk is None:
            return Response('Primary Key is None', status=status.HTTP_404_NOT_FOUND)
        account = get_object_or_404(Account, pk=pk)
        return Response({account.getPassword()})
    
router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet, 'account')
