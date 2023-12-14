from django.contrib import admin
from django.urls import path

from .views import PaymentListView, PaymentDetailView


urlpatterns = [
    path('payment/', PaymentListView.as_view(), name='payment-list'),
    path('payment/<int:id>', PaymentDetailView.as_view(), name='payment'),
]
