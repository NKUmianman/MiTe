# Generated by Django 4.2 on 2023-06-01 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_remove_userinfo_age_remove_userinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinfo',
            name='id',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, verbose_name='订单号'),
        ),
    ]