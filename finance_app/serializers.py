from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Expense, Income

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'user', 'category', 'amount', 'date')

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ('id', 'user', 'amount', 'date')
