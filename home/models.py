from django.db import models

# Create your models here.

class FunnelStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    status = models.ForeignKey(FunnelStatus, on_delete=models.CASCADE, related_name='customers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CustomerLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='logs')
    status = models.ForeignKey(FunnelStatus, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.status.name}"
