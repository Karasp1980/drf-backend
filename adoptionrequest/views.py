from rest_framework import generics, permissions, serializers
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Adoptionrequest
from .serializers import AdoptionrequestSerializer, AdoptionrequestDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend



class AdoptionrequestList(generics.ListCreateAPIView):
    """
    List adoptionrequests or create an adoptionrequest if logged in.
    """
    serializer_class = AdoptionrequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adoptionrequest.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['adoption__owner__profile']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AdoptionrequestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a adoptionequest, or update or delete it by id.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdoptionrequestDetailSerializer
    queryset = Adoptionrequest.objects.all()
   