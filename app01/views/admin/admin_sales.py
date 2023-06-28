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

class SalesModelForm(BootStrapModelForm):
    class Meta:
        model = models.SalesInfo
        fields = "__all__"
        exclude = ["create_time"]



class SalesEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.SalesInfo
        fields = "__all__"
        exclude = ["id","create_time"]

def sales_list(request):
    # 获取用户表单信息
    form = SalesModelForm()

    # 搜索
    data_dict = {}
    search_data = request.GET.get("search", '')
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.SalesInfo.objects.filter(**data_dict).order_by("id")

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
    return render(request, 'admin_sales.html', context)



@csrf_exempt
def sales_add(request):
    form = SalesModelForm(data=request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.create_time = datetime.datetime.now().date()
        user.save()
        return JsonResponse({"status": True})
    else:
        return JsonResponse({"status": False, "error": form.errors})

def sales_delete(request):
    uid = request.GET.get("uid")
    models.SalesInfo.objects.filter(id=uid).delete()
    return JsonResponse({"status": True, "error": "数据不存在"})

def sales_detail(request):
    uid = request.GET.get("uid")
    row_dict = models.SalesInfo.objects.filter(id=uid).values("good","buyer","seller","state").first()

    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    else:
        return JsonResponse({"status": True, "data": row_dict})

@csrf_exempt
def sales_edit(request):
    uid = request.GET.get("uid")
    print(uid)
    row_object = models.SalesInfo.objects.filter(id=uid).first()
    form = SalesEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    else:
        return JsonResponse({"status": False, "error": form.errors})
