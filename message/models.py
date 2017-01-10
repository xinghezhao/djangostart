# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(max_length=50, primary_key=True, verbose_name=u'主键', default='')
    name = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name = u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'联系地址')


    class Meta:
        verbose_name = u'用户留言信息'
        verbose_name_plural = verbose_name  #显示复数信息，如果不添加会在用户留言后面加一个s



        # db_table = 'user_message' #数据表的前缀显示
        # ordering = '-object_id' #排序
