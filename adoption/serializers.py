from rest_framework import serializers
from adoption.models import Adoption
from adoptionlikes.models import Adoptionlike


class AdoptionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    adoptionlike_id = serializers.SerializerMethodField()
    adoptionlikes_count = serializers.ReadOnlyField()
    adoptioncomments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            adoptionlike = Adoptionlike.objects.filter(owner=user, adoption=obj).first()
            return adoptionlike.id if adoptionlike else None
        return None

    class Meta:
        model = Adoption
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'adoptionlike_id', 'adoptionlikes_count', 'adoptioncomments_count', 'breed', 'location', 'sex', 'age'
        ]