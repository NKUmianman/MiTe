# Generated by Django 4.2 on 2023-05-25 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('男', '男'), ('女', '女')], max_length=4, verbose_name='性别'),
        ),
    ]
