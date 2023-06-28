from django.shortcuts import render
from app01 import models

def home(request):

    usernum=models.UserInfo.objects.count()
    salesnum=models.SalesInfo.objects.count()
    return render(request, 'admin_home.html',{"usernum":usernum,"salesnum":salesnum})