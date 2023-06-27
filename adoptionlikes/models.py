from django.db import models
from django.contrib.auth.models import User
from adoption.models import Adoption


class Adoptionlike(models.Model):
    """
    Adoptionlike model, related to 'owner' and 'adoption'.
    'owner' is a User instance and 'adoption' is a Adoption instance.
    'unique_together' makes sure a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    adoption = models.ForeignKey(
        Adoption, related_name='adoptionlikes',on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'adoption'] 

    def __str__(self):
        return f'{self.owner} {self.adoption}'
