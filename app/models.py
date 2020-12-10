from django.db import models

# Create your models here.
from django.db import models
#实例：创建一个user模型类
class User(models.Model):#模型类必须继承于models.Model,定义了自增的id
    name=models.CharField(max_length=10,unique=True)#charfield 字符串
    passingcode=models.CharField(max_length=20)
    create_time=models.DateTimeField(auto_now_add=True)
    email=models.CharField(max_length=20)
    #定义嵌套类，定义数据表名称、查询规则等
    class Meta:
        db_table='user'
