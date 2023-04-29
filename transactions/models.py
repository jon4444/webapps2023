from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     name = models.CharField(max_length=50)
#     amount = models.IntegerField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         details = ''
#         details += f'Username : {self.name}\n'
#         details += f'Amount  : {self.balance}\n'
#         return details
    
    
    
class Money(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1000)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.user.username} - {self.amount} amount"

class MoneyTransfer(models.Model):
    enter_your_username = models.CharField(max_length=50)
    enter_destination_username = models.CharField(max_length=50)
    enter_amount_to_transfer = models.IntegerField()

    def __str__(self):
        return f"{self.enter_your_username} transferred {self.enter_amount_to_transfer} amount to {self.enter_destination_username}"
    
class MoneyRequest(models.Model):
    enter_your_username = models.CharField(max_length=50)
    enter_destination_username = models.CharField(max_length=50)
    enter_amount_to_request = models.IntegerField()
    
    