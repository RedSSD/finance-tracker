from rest_framework import generics
from payment.models import Payment


class PaymentListView(generics.ListAPIView):
    model = Payment


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Payment


class PaymentCreateView(generics.CreateAPIView):
    model = Payment
