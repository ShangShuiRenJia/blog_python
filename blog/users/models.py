from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# 用户信息
class User(AbstractUser):
    # 电话号码字段   unique：唯一，blank：必填
    mobile = models.CharField(max_length=11, unique=True, blank=False)
    # 头像   blank：可选
    avatar = models.ImageField(upload_to='avatar/%Y%m%d/', blank=True)
    # 简介信息
    user_desc = models.TextField(max_length=500, blank=True)

    # USERNAME_FIELD = 'mobile'

    # REQUIRED_FIELDS = ['username', 'email']

    # 修改配置信息
    class Meta:
        db_table = 'tb_user'   # 修改表名
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name   # admin后台显示

    def __str__(self):
        return self.mobile

