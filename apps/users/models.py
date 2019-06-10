from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=20, verbose_name="用户名")
    upass = models.CharField(max_length=50, verbose_name="密码")
    phone = models.CharField(max_length=23, verbose_name="电话")
    email = models.EmailField(null=True, blank=True,default="", verbose_name="邮箱")
    class Meta:
        verbose_name = u'登陆用户信息'
        verbose_name_plural = verbose_name
        db_table = "user"

class Group(models.Model):
    gname = models.CharField(max_length=20, verbose_name="组名")
    #user_group = models.ForeignKey("User", on_delete=models.CASCADE)
    class Meta:
        verbose_name = u'用户组信息'
        verbose_name_plural = verbose_name
        db_table = "group"

