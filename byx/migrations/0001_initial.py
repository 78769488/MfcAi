# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-12 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, verbose_name='代码')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('gains', models.CharField(max_length=32, verbose_name='涨幅')),
                ('closing', models.CharField(max_length=32, verbose_name='收盘')),
                ('turnover', models.CharField(max_length=32, verbose_name='成交量')),
                ('totalMoney', models.CharField(max_length=32, verbose_name='总金额')),
                ('pressure', models.CharField(max_length=32, verbose_name='压力')),
                ('support', models.CharField(max_length=32, verbose_name='支撑')),
                ('tPressure', models.CharField(max_length=32, verbose_name='明日压力')),
                ('tSupport', models.CharField(max_length=32, verbose_name='明日支撑')),
                ('dataDate', models.DateField(verbose_name='数据日期')),
                ('nextDate', models.DateField(verbose_name='下个交易日')),
                ('upTime', models.DateTimeField(verbose_name='数据更新时间')),
                ('upUser', models.CharField(max_length=32, verbose_name='数据更新者')),
            ],
            options={
                'verbose_name': '基本数据',
                'verbose_name_plural': '基本数据',
            },
        ),
        migrations.CreateModel(
            name='Futures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(max_length=32, verbose_name='上市交易所')),
                ('veriety', models.CharField(max_length=32, verbose_name='品种分类')),
                ('name', models.CharField(max_length=32, verbose_name='期货名称')),
                ('code', models.CharField(max_length=32, verbose_name='期货代码')),
            ],
            options={
                'verbose_name': '品种信息',
                'verbose_name_plural': '品种信息',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=32, verbose_name='期货名称')),
                ('pname', models.CharField(max_length=32, verbose_name='其他名称')),
            ],
            options={
                'verbose_name': '其他名称',
                'verbose_name_plural': '其他名称',
            },
        ),
        migrations.CreateModel(
            name='Tj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('type', models.CharField(max_length=32, verbose_name='上行类别')),
                ('counts', models.IntegerField(verbose_name='上行次数')),
            ],
            options={
                'verbose_name': '数据统计',
                'verbose_name_plural': '数据统计',
            },
        ),
    ]
