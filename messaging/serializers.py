from rest_framework import serializers
from .models import Messaging


class MessagingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Messaging model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Messaging
        fields = [
            'id', 'owner', 'is_owner', 'message', 'created_at',
            'updated_at', 'profile', 'profile_id', 'profile_image',
        ]


class MessagingDetailSerializer(MessagingSerializer):
    """
    Serializer for the Messaging model used in Detail view
    profile is a read only field so that we dont have to set it on each update
    """
    profile = serializers.ReadOnlyField(source='profile.id')