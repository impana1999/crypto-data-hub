import uuid
from django.db import models
from django.contrib.auth.models import User 
class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class CryptoPrice(models.Model):
    id = models.AutoField(primary_key=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)  
    price = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)
