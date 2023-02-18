from django.shortcuts import render
from django.http import HttpResponse

def tenant_page(request):
    return render(request, "tenants.html")