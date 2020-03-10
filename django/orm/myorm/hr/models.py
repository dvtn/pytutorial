from django.db import models


# Create your models here.

class Employee(models.Model):
    DEPARTMENTS = (
        ('管理部', '管理部'),
        ('营销部', '营销部'),
        ('财务部', '财务部'),
        ('业务部', '业务部'),
        ('生产部', '生产部'),
    )
    name = models.CharField(verbose_name='姓名', max_length=20)
    id_card = models.CharField('身份证号', max_length=20)
    department = models.CharField('部门', choices=DEPARTMENTS, max_length=20)
    salary = models.DecimalField('薪资', max_digits=9, decimal_places=2)
    address = models.CharField('地址', max_length=200, null=True)
    telephone = models.CharField('电话', max_length=20)
    postal_code = models.CharField('邮编', max_length=6)
    birthdate = models.DateField('生日')

    class Meta:
        ordering = ['department', '-salary']
        get_latested_by='birthdate'

    def __str__(self):
        return f'{self.id} {self.name} {self.department} {self.salary}'
