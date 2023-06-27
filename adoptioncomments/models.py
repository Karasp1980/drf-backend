from django.db import models
from django.contrib.auth.models import User
from adoption.models import Adoption


class Adoptioncomment(models.Model):
    """
    Adoptioncomment model, related to User and Adoption
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    adoption = models.ForeignKey(Adoption, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content