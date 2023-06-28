from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from app01 import models

def login(request):

    return render(request, 'login-register.html')

@csrf_exempt
def login_check(request):
    account=request.POST.get("account")
    password=request.POST.get("password")
    exists=models.UserInfo.objects.filter(account=account,password=password).exists()
    if exists:
        user = models.UserInfo.objects.filter(account=account, password=password).first()
        return render(request,"home.html",{"name": user.name})
    return render(request,"login-register.html",{"error": "用户名或密码错误"})


