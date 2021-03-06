from django.shortcuts import render, HttpResponse
from django.db import connection
# Create your views here.
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from byx.serializers import UserSerializers, GroupSerializer
import re
import json
from byx import models


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     允许查看和编辑user的API endpoint
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     允许查看和编辑group的API endpoint
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


def index(request):
    print("index", request.method, request.GET.get('para'), )
    return render(request,
                  "ai.html",)


def query(request):
    print(request.method, request.GET.get('para'), )
    para = request.GET.get("para")  # 获取用户输入的内容
    # 不需要查库的操作
    if para == "index":
        ret = {"messages":
                   [{"t": "0",
                     "msg": "我是贴心为你服务的客服小美。"
                     },
                    {"t": "1",
                     "msg": "这是否是您需要的问题:<br><a href='javascript:void(0);' onclick='set_para('宝盈线');'>宝盈线是什么？<br></a><a href='javascript:void(0);' onclick='set_para('铜主力');'><font color=#ff1400>铜主力合约</font>的明日压力位和支撑位？</a><br><a href='javascript:void(0);' onclick='set_para('中国中车');'><font color=#ff1400>中国中车</font>的明日压力位和支撑位？</a><br>"
                     },
                    {"t": "0",
                     "msg": "输入关键字查询宝盈线（例如：CU、铜、中国中车、601766）"
                     }
                    ]
               }
    elif para == "宝盈线":
        ret = {"messages":
                   [{"t": "0",
                     "msg": "宝盈线是由每日支撑位和压力位相连接构成的策略图形。根据趋势信号预判每日支撑位和压力位，为您提供合理的投资建议。"
                     }
                    ]
               }
    else:  # 需要查库的操作
        if para.isdigit():  # 全数字为股票代码
            if len(para) == 6:
                ret = {"messages":
                           [{"t": "0",
                             "msg": query_stock(para)}
                            ]
                       }
            else:
                ret = {"messages":
                           [{"t": "0", "msg": "错误的股票代码!"}
                            ]
                       }
        else:  # 非数字--> 查询股票或期货
            # 先匹配期货信息
            if len(para) > 2 and para.endswith("主力"):  # 查询主力合约
                ret = {"messages":
                           [{"t": "0",
                             "msg": query_futures_name(para)}
                            ]
                       }
            elif len(para) > 2 and para.endswith("指数"):  # 查询主力合约
                ret = {"messages":
                           [{"t": "0",
                             "msg": query_futures_name(para)}
                            ]
                       }
            elif re.match(r'\w+\d+', para):  # 匹配字母和数字并且是以数字结尾的字符串, 此次为期货信息
                ret = {"messages":
                           [{"t": "0",
                             "msg": query_futures_code(para)}
                            ]
                       }

            else:
                ret = {"messages":
                           [{"msg": "您的关键词不太详细哦，再告诉小美一次吧!"}
                            ]
                       }
    return HttpResponse("%s" % json.dumps(ret))


def query_stock(para):
    """
    股票查询
    :param para: 股票代码或者股票名称
    :return: 查询结果
    """
    data = models.Data.objects.filter(code=para).first()
    if data:
        ret = "代码:{code}<br>名称:{name}<br>涨幅:{gains}<br>收盘:{closing}<br>成交量:{turnover}<br>总金额:{totalMoney}<br>" \
              "{today}压力:{pressure}<br>{today}支撑:{support}<br>{tomorrow}压力:{tPressure}<br>{tomorrow}支撑:{tSupport}<br>"
        dic = dict(code=data.code, name=data.name, gains=data.gains, closing=data.closing, turnover=data.turnover,
                   totalMoney=data.totalMoney, pressure=data.pressure, support=data.support, tPressure=data.tPressure,
                   tSupport=data.tSupport, today=date2str(data.dataDate), tomorrow=date2str(data.nextDate))
        return ret.format(**dic)
    else:
        return "您的关键词不太详细哦，再告诉小美一次吧!"


def query_futures_name(para):
    """
    期货主力合约及指数(名称)查询
    :param para: 
    :return: 
    """
    data = models.Data.objects.filter(name__iendswith=para).first()
    print(connection.queries)
    if data:
        ret = "代码:{code}<br>名称:{name}<br>涨幅:{gains}<br>收盘:{closing}<br>成交量:{turnover}<br>总金额:{totalMoney}<br>" \
              "{today}压力:{pressure}<br>{today}支撑:{support}<br>{tomorrow}压力:{tPressure}<br>{tomorrow}支撑:{tSupport}<br>"
        dic = dict(code=data.code, name=data.name, gains=data.gains, closing=data.closing, turnover=data.turnover,
                   totalMoney=data.totalMoney, pressure=data.pressure, support=data.support, tPressure=data.tPressure,
                   tSupport=data.tSupport, today=date2str(data.dataDate), tomorrow=date2str(data.nextDate))
        return ret.format(**dic)
    else:
        return "您的关键词不太详细哦，再告诉小美一次吧!"


def query_futures_code(para):
    """
    期货主力合约及指数(代码)查询
    :param para: 
    :return: 
    """
    data = models.Data.objects.filter(code__icontains=para).first()
    print(connection.queries)
    if data:
        ret = "代码:{code}<br>名称:{name}<br>涨幅:{gains}<br>收盘:{closing}<br>成交量:{turnover}<br>总金额:{totalMoney}<br>" \
              "{today}压力:{pressure}<br>{today}支撑:{support}<br>{tomorrow}压力:{tPressure}<br>{tomorrow}支撑:{tSupport}<br>"
        dic = dict(code=data.code, name=data.name, gains=data.gains, closing=data.closing, turnover=data.turnover,
                   totalMoney=data.totalMoney, pressure=data.pressure, support=data.support, tPressure=data.tPressure,
                   tSupport=data.tSupport, today=date2str(data.dataDate), tomorrow=date2str(data.nextDate))
        return ret.format(**dic)
    else:
        return "您的关键词不太详细哦，再告诉小美一次吧!"


def date2str(dt):
    return "{}年{}月{}日".format(dt.year, dt.month, dt.day)


