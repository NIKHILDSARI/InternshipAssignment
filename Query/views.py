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
    Banks_Queryset = Banks.objects.all()
    for bank in Banks_Queryset:
        bank_dict = serializers.serialize("python", [bank])[0]['fields']
        context[bank.id] = bank_dict
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
    for selected_bank_branch_details  in selected_branch_queryset:
        selected_bank_branch_details_dict = serializers.serialize('python', [selected_bank_branch_details],fields=('branch',
                                                                                                                   'address',
                                                                                                                   'city',
                                                                                                                   'district',
                                                                                                                   'state') )[0]['fields']
        selected_bank_branch_details_dict['ifsc'] = selected_bank_branch_details.ifsc
        print(selected_bank_branch_details_dict)
        context[selected_bank_branch_details.branch] = selected_bank_branch_details_dict
    return JsonResponse(context,safe=False)

@csrf_exempt
def spicific_Branchdetails(request):
    context = {}
    json_data = json.loads(request.body)
    Branch = json_data['Branch']
    selected_branch_queryset = Branches.objects.filter(branch = Branch)
    if not selected_branch_queryset:
        return JsonResponse({'error':'Branch not found , Make sure that ' + str(Branch) + ' exits'})
    for selected_bank_branch_details  in selected_branch_queryset:
        selected_bank_branch_details_dict = serializers.serialize('python', [selected_bank_branch_details],fields=('branch',
                                                                                                                   'address',
                                                                                                                   'city',
                                                                                                                   'district',
                                                                                                                   'state') )[0]['fields']
        selected_bank_branch_details_dict['ifsc'] = selected_bank_branch_details.ifsc
        print(selected_bank_branch_details_dict)
        context[selected_bank_branch_details.branch] = selected_bank_branch_details_dict
    return JsonResponse(context,safe=False)
