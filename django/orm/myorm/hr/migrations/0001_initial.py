# Generated by Django 3.0.4 on 2020-03-08 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('id_card', models.CharField(max_length=20, verbose_name='身份证号')),
                ('department', models.CharField(choices=[('管理部', '管理部'), ('营销部', '营销部'), ('财务部', '财务部'), ('业务部', '业务部'), ('生产部', '生产部')], max_length=20, verbose_name='部门')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='薪资')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='地址')),
                ('telephone', models.CharField(max_length=20, verbose_name='电话')),
                ('postal_code', models.CharField(max_length=6, verbose_name='邮编')),
                ('birthdate', models.DateField(verbose_name='生日')),
            ],
            options={
                'ordering': ['department', '-salary'],
            },
        ),
    ]
