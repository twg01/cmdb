import time

from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def get_inventory(request, id):
    id = str(id)
    html = {
        "1": "inventory/default.html",
        "2": "inventory/all_inventory.html",
        "3": "inventory/phymachine.html",
        "4": "inventory/virmachine.html",
        "5": "inventory/netmachine.html",
        "6": "inventory/othermachine.html"
    }

    curtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # objdb = HostInfo.objects.all()
    # if id == "1":
    #     physicdata = PhysicInfo.objects.all().values()
    #     datas = physicdata.values( 'device_number', 'sn', 'position', 'warranty',
    #                               'hostinfo__ip','hostinfo__os','hostinfo__inventory_name','hostinfo__application','hostinfo__manager'
    #                               )
    #     datahead = { 'device_number':'设备型号', 'sn':'序列号', 'position':'机房位置', 'warranty':'保修日期','ip':'ip地址'}
    # elif id == "2":
    #     pass
    # elif id == "3":
    #     vritualdata = VirtualInfo.objects.all()
    #     # datas = vritualdata.values()
    #     # print(datas)
    #     # datahead = datas[0]
    # elif id == "4":
    #     pass

    return render(request, html.get(id), context=locals())
    # return render(request, "inventory.html", locals())

def operatelog(request):
    return HttpResponse("<p>等待更新...</p>")


