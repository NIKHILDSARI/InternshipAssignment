from .models import *
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

@csrf_exempt
def Banklist(request):
    context = {}
    bank_dict = {}
    Banks_Queryset = Banks.objects.all()
    for bank in Banks_Queryset:
        bank_dict[bank.id] = serializers.serialize("python", [bank])[0]['fields']['name']
    context['bank_id'] = bank_dict
    return JsonResponse(context,safe=False)
    

@csrf_exempt
def Branchdetails(request):
    context = {}
    json_data = json.loads(request.body)
    Bank = json_data['Bank']
    Branch = json_data['Branch']
    bank_object = Banks.objects.get(name = Bank)
    selected_branch_queryset = Branches.objects.filter(Q(bank=bank_object) & Q(branch = Branch))
    if not selected_branch_queryset:
        return JsonResponse({'error':'Branch not found , Make sure that ' + str(Bank) + ' has ' + str(Branch) +  ' as its Branch'})
    selected_bank_branch_details_dict={}
    for selected_bank_branch_details  in selected_branch_queryset:
        selected_bank_branch_details_dict[selected_bank_branch_details.ifsc] = serializers.serialize('python', [selected_bank_branch_details],fields=('branch',
                                                                                                                   'address',
                                                                                                                   'city',
                                                                                                                   'district',
                                                                                                                   'state') )[0]['fields']
        
    context[Bank] = selected_bank_branch_details_dict
    return JsonResponse(context,safe=False)

@csrf_exempt
def specific_Branchdetails(request):
    context = {}
    json_data = json.loads(request.body)
    Branch = json_data['Branch']
    Branches.objects.filter().select_related() 
    selected_branch_queryset = Branches.objects.filter(branch = Branch)
    if not selected_branch_queryset:
        return JsonResponse({'error':'Branch not found , Make sure that ' + str(Branch) + ' exits'})
    selected_bank_branch_details_dict={}
    for selected_bank_branch_details  in selected_branch_queryset:
        
        selected_bank_branch_details_dict[selected_bank_branch_details.ifsc] = serializers.serialize('python', [selected_bank_branch_details],fields=('branch',
                                                                                                                   'address',
                                                                                                                   'city',
                                                                                                                   'district',
                                                                                                                   'state') )[0]['fields']
        bank_name = Banks.objects.get(id = selected_bank_branch_details.bank_id)
        selected_bank_branch_details_dict[selected_bank_branch_details.ifsc]['bank_name'] = serializers.serialize("python", [bank_name])[0]['fields']['name']
    context[Branch] = selected_bank_branch_details_dict
    return JsonResponse(context,safe=False)
