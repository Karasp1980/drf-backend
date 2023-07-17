from rest_framework import serializers
from .models import Adoptionrequest
from adoption.models import Adoption


class AdoptionrequestSerializer(serializers.ModelSerializer):
    """
    Serializer for the Adoptionrequest model
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
    
    adoption = serializers.ReadOnlyField(source='adoption.id')

    class Meta:
        model = Adoptionrequest
        fields = [
            'id', 'owner', 'is_owner', 'name', 'phone', 'email', 'adoptionmessage', 'created_at',
            'updated_at', 'profile', 'profile_id', 'profile_image','adoption',
        ]
   

class AdoptionrequestDetailSerializer(AdoptionrequestSerializer):
    """
    Serializer for the Adoptionrequest model used in Detail view
    profile is a read only field so that we dont have to set it on each update
    """
    profile = serializers.ReadOnlyField(source='profile.id')