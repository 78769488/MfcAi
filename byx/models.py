from django.db import models


# Create your models here.
class Data(models.Model):
    """期市、股市基本数据信息"""
    code = models.CharField(max_length=32, verbose_name="代码")
    name = models.CharField(max_length=32, verbose_name="名称")
    gains = models.FloatField(max_length=32, verbose_name="涨幅")
    closing = models.FloatField(max_length=32, verbose_name="收盘")
    turnover = models.CharField(max_length=32, verbose_name="成交量")
    totalMoney = models.CharField(max_length=32, verbose_name="总金额")
    pressure = models.FloatField(max_length=32, verbose_name="压力")
    support = models.FloatField(max_length=32, verbose_name="支撑")
    tPressure = models.FloatField(max_length=32, verbose_name="明日压力")
    tSupport = models.FloatField(max_length=32, verbose_name="明日支撑")
    dataDate = models.DateField(verbose_name="数据日期")
    nextDate = models.DateField(verbose_name="下个交易日")
    dataType = models.IntegerField(verbose_name="数据类型,0: 股票, 1期货")
    upTime = models.DateTimeField(verbose_name="数据更新时间")
    upUser = models.CharField(max_length=32, verbose_name="数据更新者")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "基本数据"
        verbose_name_plural = "基本数据"

        # 联合唯一索引
        unique_together = (("code", "name"),)


class Product(models.Model):
    """品种信息，用户检索识别品种或者常用名称等"""
    name = models.CharField(max_length=32, verbose_name="名称")
    code = models.CharField(max_length=32, verbose_name="代码")

    exchange = models.ForeignKey(to="Exchanges")
    veriety = models.ForeignKey(to="Verieties")

    def __str__(self):
        return "%s: %s" % (self.code, self.name)

    class Meta:
        verbose_name = "品种信息"
        verbose_name_plural = "品种信息"


class OtherPrdNmae(models.Model):
    """其他名称"""
    name = models.CharField(max_length=32, verbose_name="名称")
    type = models.CharField(max_length=32, verbose_name="类型: 合约正式名, 别名别称")

    def __str__(self):
        return "%s: %s" % (self.name, self.type)

    class Meta:
        verbose_name = "其他名称"
        verbose_name_plural = "其他名称"


class Exchanges(models.Model):
    """交易所信息"""
    name = models.CharField(max_length=32, verbose_name="上市交易所")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "交易所信息"
        verbose_name_plural = "交易所信息"


class Verieties(models.Model):
    """品种分类"""
    name = models.CharField(max_length=32, verbose_name="品种分类")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "品种分类"
        verbose_name_plural = "品种分类"


class Tj(models.Model):
    """用户交互的统计结果，统计每天的交互量，上下行，分期货、股票、品种类别、无法识别等类别，以及总量"""
    user = models.CharField(max_length=32, verbose_name="用户")
    date = models.DateField(verbose_name="日期")
    type = models.CharField(max_length=32, verbose_name="上行类别")
    counts = models.IntegerField(verbose_name="上行次数")

    def __str__(self):
        return "%s-%s-%s-%s" % (self.user, self.date, self.type, self.counts)

    class Meta:
        verbose_name = "数据统计"
        verbose_name_plural = "数据统计"
