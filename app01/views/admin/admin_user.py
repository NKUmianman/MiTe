from django.shortcuts import render, redirect
from django.http import JsonResponse
from app01 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from app01.utils.Pagination import Pagination
from app01.utils.BootStrap import BootStrapModelForm
import datetime


class UserModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        exclude = ["create_time"]

    # 验证账号的钩子
    def clean_account(self):
        txt_account = self.cleaned_data["account"]
        exists = models.UserInfo.objects.filter(account=txt_account).exists()
        if exists:
            raise ValidationError("该账号已存在")
        return txt_account


class UserEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        exclude = ["create_time"]

    # 验证账号的钩子
    def clean_account(self):
        txt_account = self.cleaned_data["account"]
        exists = models.UserInfo.objects.filter(account=txt_account).exclude(id=self.instance.pk).exists()
        if exists:
            raise ValidationError("该账号已存在")
        return txt_account


def user_list(request):
    # 获取用户表单信息
    form = UserModelForm()

    # 搜索
    data_dict = {}
    search_data = request.GET.get("search", '')
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.UserInfo.objects.filter(**data_dict).order_by("id")

    # 分页
    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    context = {
        "queryset": page_queryset,
        "search_data": search_data,
        "page_string": page_string,
        "form": form,
    }
    return render(request, 'admin_user.html', context)


@csrf_exempt
def user_add(request):
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.create_time = datetime.datetime.now().date()
        user.save()
        return JsonResponse({"status": True})
    else:
        return JsonResponse({"status": False, "error": form.errors})


def user_delete(request):
    uid = request.GET.get("uid")
    models.UserInfo.objects.filter(id=uid).delete()
    return JsonResponse({"status": True, "error": "数据不存在"})


def user_detail(request):
    uid = request.GET.get("uid")
    row_dict = models.UserInfo.objects.filter(id=uid).values("name", "account", "password").first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    else:
        return JsonResponse({"status": True, "data": row_dict})


@csrf_exempt
def user_edit(request):
    uid = request.GET.get("uid")
    print(uid)
    row_object = models.UserInfo.objects.filter(id=uid).first()
    form = UserEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    else:
        return JsonResponse({"status": False, "error": form.errors})


@csrf_exempt
def user_register(request):
    form=UserModelForm()
    user = form.save(commit=False)
    user.name=request.GET.get('name')
    user.account=request.GET.get('account')
    user.password=request.GET.get('password')
    user.create_time = datetime.datetime.now().date()

    user.save()
    return redirect("/login/")

@csrf_exempt
def user_login(request):
    form=UserModelForm()
    user=form.save(commit=False)
    user.account=request.GET.get('account')
    user.password=request.GET.get('password')
    exists = models.UserInfo.objects.filter(account=user.account,password=user.password).exists()
    if exists:
        return redirect("/login/")
