from django.forms import ModelForm
from transactions.models import MoneyTransfer, MoneyRequest

class MoneytransferForm(ModelForm):
    class Meta:
        model = MoneyTransfer
        fields = ["enter_your_username", "enter_destination_username", "enter_amount_to_transfer"]
        
class MoneyRequestForm(ModelForm):
    class Meta:
        model = MoneyRequest
        fields = ["enter_your_username", "enter_destination_username", "enter_amount_to_request"]