from django.db import models

class Client(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

class Subscription(models.Model):
    client = models.ForeignKey(Client, related_name='subscriptions', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='active')  # active, expired, cancelled

    def __str__(self):
        return f"{self.client.full_name} : {self.start_date} -> {self.end_date}"
