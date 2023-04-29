from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from transactions.models import Money


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    CURRENCY = (
        ('GBP', 'Pounds'),
        ('USD', 'Dollar'),
        ('EUR', 'EUROS')
    )
    
    currency = forms.ChoiceField(choices=CURRENCY)

    class Meta:
        model = User
        fields = ["username", "currency", "email", "password1", "password2"]

    def save(self, *args, **kwargs):
        instance = super(RegisterForm, self).save(*args, **kwargs)
        Money.objects.create(user=instance, amount=1000, currency=self.cleaned_data['currency'])
        return instance