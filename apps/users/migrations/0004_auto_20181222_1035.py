# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-22 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181115_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')], max_length=20),
        ),
    ]