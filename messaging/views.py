from rest_framework import generics, permissions
from events_api.permissions import IsOwnerOrReadOnly
from .models import Messaging
from .serializers import MessagingSerializer, ContactDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MessagingList(generics.ListCreateAPIView):
    """
    List message or create a message if logged in.
    """
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profile']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MessagingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a message, or update or delete it by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactDetailSerializer
    queryset = Contact.objects.all()
