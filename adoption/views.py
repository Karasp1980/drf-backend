from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Adoption
from .serializers import AdoptionSerializer


class AdoptionList(generics.ListCreateAPIView):
    """
    List adoption posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = AdoptionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adoption.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
   
    search_fields = [
    'owner__username',
    'title',
    'sex',
    'location',
    'age',
    'content',
    'created_at',
    'likes_count',
    'comments_count',
    'likes__created_at',
]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdoptionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = AdoptionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Adoption.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
