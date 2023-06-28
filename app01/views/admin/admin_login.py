from django.shortcuts import redirect, render

from django import forms
from app01 import models
from app01.utils.encrypt import md5


class LoginForm(forms.Form):
    account = forms.CharField(
        label="账号",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}, render_value=True),
    )


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'admin_login.html', {"form": form})
    else:
        form = LoginForm(data=request.POST)

        if form.is_valid():
            # 去数据库校验用户名和密码是否正确
            admin_object = models.AdminInfo.objects.filter(**form.cleaned_data).first()
            if not admin_object:
                # 让错误信息显示在密码下面
                form.add_error("password", "用户名或密码错误")
                return render(request, 'admin_login.html', {"form": form})
            # 如果用户名和密码正确
            # 网站生成随机字符串，写到用户浏览器的cookie中，再写入到session中
            request.session["info"] = {'id': admin_object.id, 'account': admin_object.account}
            return redirect('/admin/home/')

        return render(request, 'admin_login.html', {"form": form})


# 注销
def logout(request):
    request.session.clear()
    return redirect('/admin/login/')
