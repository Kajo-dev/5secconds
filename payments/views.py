from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from product_store.models import Cart

@login_required(login_url='login_page')
def transaction_confirmed(request):
    body = json.loads(request.body)
    
    return JsonResponse('Payment completed!', safe=False)