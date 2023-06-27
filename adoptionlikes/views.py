from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from adoptionlikes.models import Adoptionlike
from adoptionlikes.serializers import AdoptionlikeSerializer


class AdoptionlikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AdoptionlikeSerializer
    queryset = Adoptionlike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdoptionlikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AdoptionlikeSerializer
    queryset = Adoptionlike.objects.all()
