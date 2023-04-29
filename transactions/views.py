from django.shortcuts import render
from django.contrib import messages
from django.db import transaction
from . import models
from transactions.forms import MoneytransferForm, MoneyRequestForm

# Create your views here.
def money_transfer(request):
    if request.method == 'POST':
        form = MoneytransferForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    print(form.cleaned_data)
                    form.save()
                    
                    src_username = form.cleaned_data["enter_your_username"]
                    dst_username = form.cleaned_data["enter_destination_username"]
                    amount_to_transfer = form.cleaned_data["enter_amount_to_transfer"]

                    src_amount = models.Money.objects.get(user__username=src_username)
                    src_amount.amount = src_amount.amount - amount_to_transfer
                    src_amount.save()

                    dst_amount = models.Money.objects.get(user__username=dst_username)
                    dst_amount.amount = dst_amount.amount + amount_to_transfer
                    dst_amount.save()

                    return render(request, "transactions/money.html", {"src_amount":
                                                                        src_amount, "dst_amount": dst_amount})
                    
            except:
                messages.error(request, "Invalid Transaction")
    else:
        form = MoneytransferForm()

    return render(request, "transactions/moneytransfer.html", {"form":form})


def money_request(request):
    if request.method == 'POST':
        form = MoneyRequestForm(request.POST)
        if form.is_valid():
            try:
                print(111)
                with transaction.atomic():
                    print(222)
                    form.save()
                    print(333)
                    # src_username = form.cleaned_data["enter_your_username"]
                    # dst_username = form.cleaned_data["enter_destination_username"]
                    # amount_to_request = form.cleaned_data["enter_amount_to_request"]
                    
                    # src_amount = models.Money.objects.select_related().get(name__username=src_username)
                    # src_amount.amount = src_amount.amount - amount_to_request
                    # src_amount.save()
                    
                    # dst_amount = models.Money.objects.select_related().get(name__username=dst_username)
                    # dst_amount.amount = dst_amount.amount + amount_to_request
                    # dst_amount.save()
                    
                    return render(request, "transactions/request_sent.html")
                messages.sent
            except:
                messages.error(request, "Invalid Request")
    else:
        form = MoneyRequestForm()
    return render(request, "transactions/moneyrequest.html", {"form": form})

def message(request):
    return render(request, 'transactions/request_sent.html')