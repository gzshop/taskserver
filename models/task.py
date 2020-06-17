
from peewee import *
from models.base import BaseModel

class Order(BaseModel):

    """
    订单表
    """

    id = BigAutoField(primary_key=True,verbose_name="ID")

    orderid = CharField(max_length=19,verbose_name="订单ID",null=True)
    linkid = CharField(max_length=255,verbose_name="关联表集合",default="")

    userid = BigIntegerField(verbose_name="用户代码", null=True)

    amount = DecimalField(verbose_name="交易金额",max_digits=18,decimal_places=6,default=0.0)
    payamount = DecimalField(verbose_name="微信支付金额",max_digits=18,decimal_places=6,default=0.0)
    balamount = DecimalField(verbose_name="余额支付金额",max_digits=18,decimal_places=6,default=0.0)
    memo = CharField(max_length=255,verbose_name="备注",default="")

    before_status = CharField(max_length=1,verbose_name="状态,1-申请退款,2-已退款,3-拒绝退款",default="")
    refundmsg = CharField(max_length=60,verbose_name="申请退款理由!",default="")
    status = CharField(max_length=1,verbose_name="状态,0-待付款,1-已付款(待发货),2-已发货(待收货),3-已收货,4-已退款,9-取消订单,8-已删除",default="0")
    fhstatus = CharField(max_length=1,verbose_name="0-已发货,1-未发货",default="1")
    paymsg = TextField(default="")
    address = TextField(default="{}")

    use_jf = DecimalField(verbose_name="交易使用积分",max_digits=18,decimal_places=6,default=0.0)
    get_jf = DecimalField(verbose_name="获得积分",max_digits=18,decimal_places=6,default=0.0)

    isvirtual = CharField(max_length=1,verbose_name="是否都是虚拟商品 0-是,1-否",default="1")
    isthm = CharField(max_length=1,verbose_name="是否提货码兑换 0-是,1-否",default="1")

    createtime = BigIntegerField(default=0,verbose_name="订单创建时间")
    updtime = BigIntegerField(default=0)

    yf = DecimalField(verbose_name="运费",max_digits=18,decimal_places=6,default=0.0)

    kdno = CharField(max_length=60,verbose_name="快递单号",default="")
    kdname = CharField(max_length=60,verbose_name="快递公司简称",default="")

    paytype = CharField(max_length=1,verbose_name="支付方式 2-支付宝",default='2')

    mobile = None

    class Meta:
        db_table = 'order'