from django.shortcuts import render
from django.http import HttpResponseRedirect
from market.models import AppTransaction

def index(request):

    transaction_list = AppTransaction.objects.all()
    context_dict = {'transactions': transaction_list}
    response = render(request, 'payment.html', context_dict)
    return response

def pay(request, pk):
    transaction_obj = AppTransaction.objects.get(id=pk)
    if (transaction_obj.paid == False):
        transaction_obj.paid = True
        transaction_obj.save()
        print transaction_obj.paid
    return HttpResponseRedirect('/payment_sys/')