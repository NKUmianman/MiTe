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


def admin_list(request):

    # 搜索
    data_dict = {}
    search_data = request.GET.get("search", '')
    if search_data:
        data_dict["name__contains"] = search_data
    queryset = models.AdminInfo.objects.filter(**data_dict).order_by("id")

    # 分页
    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    context = {
        "queryset": page_queryset,
        "search_data": search_data,
        "page_string": page_string,
    }

    return render(request, 'admin_admin.html',context)