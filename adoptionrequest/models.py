from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from adoption.models import Adoption

class Adoptionrequest(models.Model):
    """
    Adoption request model, related to Profile
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.TextField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    adoptionmessage = models.TextField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    adoption = models.ForeignKey(Adoption, on_delete=models.CASCADE, related_name="adoption")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner}: {self.name} - Phone:{self.phone} - Email:{self.email} - Message: {self.adoptionmessage} -"
