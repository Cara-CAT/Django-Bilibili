
# login/models.py

from django.db import models


class User(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    # name必填，最长不超过128个字符，并且唯一
    password = models.CharField(max_length=256)
    # 密码必填，最长不超过256个字符
    email = models.EmailField(unique=True)
    # email使用Django内置的邮箱类型，唯一
    sex = models.CharField(max_length=32, choices=gender, default='女')
    # 性别使用了choice，只能选择男或女，默认为女
    c_time = models.DateTimeField(auto_now_add=True)
    # auto_now_add:每当对象被创建时，设为当前日期，用于保存创建日期
    # 元数据里定义用户按照创建时间的反序排列，也就是最近的最先显示


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

