from django.db import models


# Create your models here.

# 用户表
class UserInfo(models.Model):

    gender_choices=(
        ('男','男'),
        ('女','女'),
    )

    name = models.CharField(verbose_name="用户名", max_length=16)
    account = models.CharField(verbose_name="账号", max_length=64)
    password = models.CharField(verbose_name="密码", max_length=64)
    create_time = models.DateField(verbose_name="创建时间")


# 订单表
class SalesInfo(models.Model):
    id = models.CharField(verbose_name="订单号", max_length=64, primary_key=True)
    good = models.CharField(verbose_name="物品", max_length=64)
    buyer = models.CharField(verbose_name="买家", max_length=16)
    seller = models.CharField(verbose_name="卖家", max_length=16)
    create_time = models.DateField(verbose_name="创建时间")

    # 订单状态
    state_choices = (
        ("待发货", "待发货"),
        ("待签收", "待签收"),
        ("待退款", "待退款"),
    )
    state = models.CharField(verbose_name="状态", choices=state_choices, max_length=16)


# 管理员表
class AdminInfo(models.Model):
    name = models.CharField(verbose_name="管理员名", max_length=32)
    account = models.CharField(verbose_name="账号", max_length=64)
    password = models.CharField(verbose_name="密码", max_length=64)
