from django.db import models
from django.contrib.auth.models import User

import uuid
# Create your models here.
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,editable=False, default=uuid.uuid4)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)

    class Meta:
        abstract= True


class Transport(BaseModel):
    user=models.ForeignKey(User , on_delete=models.CASCADE, related_name="transforms")
    car=models.ForeignKey("Cars", on_delete=models.CASCADE)
    Path=models.TextField()
    shipment=models.ForeignKey("shipment", on_delete=models.CASCADE)
    createdate=models.DateField(auto_now_add=True)
    transport_done=models.BooleanField()
    is_done=models.BooleanField()

    def __str__(self)->str:
        return self.Path


class Cars(BaseModel):
    car_name=models.CharField(max_length=200)
    car_type=models.ForeignKey("Car_type", on_delete=models.CASCADE)
    is_used=models.BooleanField()


class Car_type(BaseModel):
    Car_type=models.CharField(max_length=200)

class shipment(BaseModel):
    shipment_name=models.TextField()
