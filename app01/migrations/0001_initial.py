# Generated by Django 4.2 on 2023-05-19 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='管理员名')),
                ('account', models.CharField(max_length=64, verbose_name='账号')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='SalesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.CharField(max_length=64, verbose_name='物品')),
                ('buyer', models.CharField(max_length=16, verbose_name='买家')),
                ('seller', models.CharField(max_length=16, verbose_name='卖家')),
                ('create_time', models.DateField(verbose_name='创建时间')),
                ('state', models.SmallIntegerField(choices=[(0, '待发货'), (1, '待签收'), (2, '待退款')], default=0, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='用户名')),
                ('account', models.CharField(max_length=64, verbose_name='账号')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('gender', models.CharField(max_length=4, verbose_name='性别')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('create_time', models.DateField(verbose_name='创建时间')),
            ],
        ),
    ]
