# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-12 03:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100, unique=True, verbose_name='主机名')),
                ('ipaddress', models.GenericIPAddressField(verbose_name='IP地址')),
                ('macaddress', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mac地址')),
                ('os_type', models.CharField(max_length=100, verbose_name='操作系统')),
                ('os_version', models.CharField(max_length=100, verbose_name='系统版本')),
                ('Manufactory', models.CharField(blank=True, max_length=50, null=True, verbose_name='设备厂商')),
                ('sn', models.CharField(max_length=64, unique=True, verbose_name='SN号')),
                ('cpu_model', models.CharField(max_length=100, verbose_name='CPU型号')),
                ('cpu_num', models.SmallIntegerField(default=0, verbose_name='物理CPU数量')),
                ('cpu_physical', models.SmallIntegerField(default=0, verbose_name='逻辑CPU数量')),
                ('memory', models.CharField(max_length=32, verbose_name='内存大小')),
                ('disk', models.CharField(max_length=255, verbose_name='硬盘大小')),
                ('status', models.SmallIntegerField(blank=True, choices=[(1, '在线'), (2, '已下线'), (3, '故障'), (4, '备用')], default=1, null=True, verbose_name='资产状态')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '主机',
                'verbose_name_plural': '主机',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='组名')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '主机组',
                'verbose_name_plural': '主机组',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='机房名称')),
                ('address', models.CharField(max_length=128, verbose_name='机房地址')),
                ('phone', models.CharField(max_length=32, verbose_name='联系电话')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('network', models.CharField(blank=True, max_length=32, null=True, verbose_name='IP地址范围')),
                ('operator', models.SmallIntegerField(choices=[(1, '电信'), (2, '联通'), (3, '移动'), (4, '铁通')], verbose_name='运营商')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('linkman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='联系人')),
            ],
            options={
                'verbose_name': 'IDC机房',
                'verbose_name_plural': 'IDC机房',
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='产品线')),
                ('slug', models.CharField(blank=True, max_length=100, null=True, verbose_name='别名')),
                ('rank', models.SmallIntegerField(default=0, verbose_name='排序')),
            ],
            options={
                'verbose_name': '产品线',
                'verbose_name_plural': '产品线',
            },
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('sn', models.CharField(blank=True, max_length=64, unique=True, verbose_name='SN号')),
                ('type', models.SmallIntegerField(choices=[(1, '路由器'), (2, '交换机'), (3, '负载均衡'), (4, 'VPN设备')], default=0, verbose_name='网络设备类型')),
                ('Manufactory', models.CharField(blank=True, max_length=50, null=True, verbose_name='设备厂商')),
                ('vlan_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='VlanIP')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内网IP')),
                ('model', models.CharField(blank=True, max_length=128, null=True, verbose_name='型号')),
                ('port_num', models.SmallIntegerField(blank=True, null=True, verbose_name='端口个数')),
                ('status', models.SmallIntegerField(blank=True, choices=[(1, '在线'), (2, '已下线'), (3, '故障'), (4, '备用')], default=0, verbose_name='资产状态')),
                ('device_detail', models.TextField(blank=True, null=True, verbose_name='详细配置')),
                ('idc', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='assets.IDC', verbose_name='所属机房')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='设备管理员')),
            ],
            options={
                'verbose_name': '网络设备',
                'verbose_name_plural': '网络设备',
            },
        ),
        migrations.CreateModel(
            name='NewAssetApprovalZone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=100, unique=True, verbose_name='主机名')),
                ('ipaddress', models.GenericIPAddressField(verbose_name='IP地址')),
                ('macaddress', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mac地址')),
                ('os_type', models.CharField(max_length=100, verbose_name='操作系统')),
                ('os_version', models.CharField(max_length=100, verbose_name='系统版本')),
                ('Manufactory', models.CharField(blank=True, max_length=50, null=True, verbose_name='设备厂商')),
                ('sn', models.CharField(blank=True, max_length=64, unique=True, verbose_name='SN号')),
                ('cpu_model', models.CharField(max_length=100, verbose_name='CPU型号')),
                ('cpu_num', models.SmallIntegerField(default=0, verbose_name='物理CPU数量')),
                ('cpu_physical', models.SmallIntegerField(default=0, verbose_name='逻辑CPU数量')),
                ('memory', models.CharField(max_length=32, verbose_name='内存大小')),
                ('disk', models.CharField(max_length=255, verbose_name='硬盘信息')),
                ('status', models.SmallIntegerField(blank=True, choices=[(1, '在线'), (2, '已下线'), (3, '故障'), (4, '备用')], default=0, null=True, verbose_name='资产状态')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('data', models.TextField(verbose_name='资产数据')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='汇报日期')),
                ('approved', models.BooleanField(default=False, verbose_name='已批准')),
                ('approved_date', models.DateTimeField(blank=True, null=True, verbose_name='批准日期')),
                ('approved_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='批准人')),
                ('idc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.IDC', verbose_name='所属机房')),
            ],
            options={
                'verbose_name': '新资产上线待批准资产',
                'verbose_name_plural': '新资产上线待批准资产',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='项目名')),
                ('slug', models.CharField(blank=True, max_length=60, null=True, verbose_name='别名')),
                ('remark', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('rank', models.SmallIntegerField(default=0, verbose_name='排序')),
                ('line', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Line', verbose_name='所属产品线')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='项目负责人')),
            ],
            options={
                'verbose_name': '业务',
                'verbose_name_plural': '业务',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='hostgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.HostGroup', verbose_name='主机组'),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.IDC', verbose_name='所属机房'),
        ),
    ]
