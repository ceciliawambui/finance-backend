from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Category, Expense, Income
from .serializers import UserSerializer, CategorySerializer, ExpenseSerializer, IncomeSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer



@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, password=password, email=email)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)
