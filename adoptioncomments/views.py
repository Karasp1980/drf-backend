from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Adoptioncomment
from .serializers import AdoptioncommentSerializer
from .serializers import AdoptioncommentDetailSerializer


class AdoptioncommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = AdoptioncommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adoptioncomment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['adoption']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdoptioncommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdoptioncommentDetailSerializer
    queryset = Adoptioncomment.objects.all()
