from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, ExpenseViewSet, IncomeViewSet, register, login

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'incomes', IncomeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += [
    path('register/', register),
    path('login/', login),
]