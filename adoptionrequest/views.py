from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Adoptionrequest
from .serializers import MessagingSerializer, MessagingDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AdoptionrequestList(generics.ListCreateAPIView):
    """
    List adoptionrequests or create an adoptionrequest if logged in.
    """
    serializer_class = AdoptionrequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adoptionrequest.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profile']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdoptionrequestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a adoptionequest, or update or delete it by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdoptionequestDetailSerializer
    queryset = Adoptionrequest.objects.all()