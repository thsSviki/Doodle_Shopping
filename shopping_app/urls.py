from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Index.as_view()),
    path('cart',Shop.as_view()),
    path('login',login.as_view()),
    path('clear', Delete.as_view()),
    path('paygate',HomePageView.as_view()),
    path('charge/', charge, name='charge')
]
