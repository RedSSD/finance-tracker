from rest_framework import generics
from payment.models import Payment
from .serialisers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated


class PaymentListView(generics.ListAPIView):
    model = Payment
    serializer_class = PaymentSerializer(many=True)
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return Payment.objects.filter(user=self.request.user, datetime=kwargs["datetime"])


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    model = Payment
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentCreateView(generics.CreateAPIView):
    model = Payment
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]