# Django REST Framework
from django.db.models import manager
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from users.serializers import UserLoginSerializer, UserModelSerializer, UserProfileSerializer, UserSignUpSerializer

# Models
from users.models import User

class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = User.objects.filter(id=int(pk))
        if not queryset:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserProfileSerializer(queryset, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)   