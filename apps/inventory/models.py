from django.db import models

# Create your models here.

# 不做表连接，仅前端使用
class ServerType(models.Model):
    name_choice = (('physical', u'物理设备'),('virtual', u'虚拟设备'),('network', u'网络设备'),('other', u'其他资产信息'))
    name = models.CharField(max_length=20,choices=name_choice ,verbose_name=u"设备名称")
    # 使用 get_type_name_display() 获取第二个值
    # p = ServerType.objects.get(id=1)
    # p.get_type_name_display()
    # '物理设备'

    class Meta:
        verbose_name = u'服务器类型'
        verbose_name_plural = verbose_name
        db_table = "servertype"

# 不做表连接，仅前端使用
class manager(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = u'负责人'
        verbose_name_plural = verbose_name
        db_table = "manager"

# 主机信息
class HostInfo(models.Model):
    state_choice = ((0, 'Down'), ('1', 'Run'), ('2', 'Unknown'))

    state = models.CharField(choices=state_choice, max_length=1, verbose_name=u"服务器状态", default=1)
    ip = models.CharField(max_length=40, verbose_name=u"IP地址", default="")
    os = models.CharField(max_length=15, verbose_name=u"操作系统", default="")
    inventory_name = models.CharField(max_length=256, default="", verbose_name=u"资产名称")
    application = models.CharField(max_length=256, default="", verbose_name=u"应用名称")
    server_type = models.CharField(max_length=20, default="None", verbose_name=u"服务器类型")
    manager = models.CharField(max_length=20, verbose_name=u"负责人")
    vender = models.CharField(max_length=30, verbose_name=u"厂商")
    ctime = models.DateTimeField(verbose_name=u"创建时间")
    mtime = models.DateTimeField(verbose_name=u"修改时间")
    comment = models.TextField(verbose_name=u"备注", default="")
    isdelete = models.BooleanField(default=0, verbose_name=u"0 未删除，1 删除")

    class Meta:
        verbose_name = u'服务器基本信息'
        verbose_name_plural = verbose_name
        db_table = "hostinfo"

class PhysicInfo(models.Model):
    device_number = models.CharField(max_length=25, verbose_name=u"设备型号")
    sn = models.CharField(max_length=25, verbose_name=u"序列号")
    position = models.CharField(max_length=15, verbose_name=u"设备位置")
    warranty = models.DateTimeField(verbose_name=u"保修日期")

    hostinfo = models.ForeignKey("HostInfo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'机房设备清单'
        verbose_name_plural = verbose_name
        db_table = "physicinfo"

class VirtualInfo(models.Model):
    vritualname = models.CharField(max_length=100, verbose_name=u"虚拟机名称")

    hostinfo = models.ForeignKey("HostInfo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'虚拟机清单'
        verbose_name_plural = verbose_name
        db_table = "virtualinfo"

class HostDetail(models.Model):
    cpuTotal = models.IntegerField()
    cpuType = models.CharField(max_length=30)
    memTotal = models.IntegerField()
    memType = models.CharField(max_length=40)
    mac = models.CharField(max_length=512, verbose_name=u"mac地址列表", default="")

    hostinfo = models.ForeignKey('HostInfo', models.CASCADE)

    class Meta:
        verbose_name = u'主机详细信息'
        verbose_name_plural = verbose_name
        db_table = "hostdetail"

class HostAccount(models.Model):
    ssh_user = models.CharField(max_length=20, verbose_name=u"用户名")
    ssh_password = models.CharField(max_length=20, verbose_name=u"密码")
    ssh_rsa = models.CharField(max_length=64, null=True, verbose_name=u"登录使用的私钥", default="")
    rsa_pass = models.CharField(max_length=64, null=True, verbose_name=u"私钥的秘药", default="")
    hostinfo = models.ForeignKey('HostInfo', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'主机账户'
        verbose_name_plural = verbose_name
        db_table = "hostaccount"



