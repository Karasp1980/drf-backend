from django.db import IntegrityError
from rest_framework import serializers
from adoptionlikes.models import Adoptionlike


class AdoptionlikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Adoptionlike model
    The create method handles the unique constraint on 'owner' and 'adoption'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Adoptionlike
        fields = ['id', 'created_at', 'owner', 'adoption']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })