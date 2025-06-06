#coding:utf-8
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='yonghuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='yonghuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yonghuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='用户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    yonghuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户姓名' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    '''
    yonghuzhanghao=VARCHAR
    mima=VARCHAR
    yonghuxingming=VARCHAR
    touxiang=Text
    xingbie=VARCHAR
    shoujihaoma=VARCHAR
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class zaihaixinxi(BaseModel):
    __doc__ = u'''zaihaixinxi'''
    __tablename__ = 'zaihaixinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jilushijian=models.DateField   (  null=True, unique=False, verbose_name='记录时间' )
    shengfen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='省份' )
    chengshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='城市' )
    juqu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='具区' )
    jingdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='经度' )
    weidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='纬度' )
    quyubianma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='区域编码' )
    jiangshuiliang=models.FloatField   (  null=True, unique=False, verbose_name='降水量(mm)' )
    jiangshuiqiangdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='降水强度(mm/h)' )
    qiwen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='气温(℃)' )
    shidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='湿度(%)' )
    renkoumidu=models.IntegerField  (  null=True, unique=False, verbose_name='人口密度(人/km²)' )
    zhibeifugaidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='植被覆盖度(%)' )
    dizhigouzao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地质构造' )
    lishishanhongjilu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='历史山洪记录' )
    '''
    jilushijian=Date
    shengfen=VARCHAR
    chengshi=VARCHAR
    juqu=VARCHAR
    jingdu=VARCHAR
    weidu=VARCHAR
    quyubianma=VARCHAR
    jiangshuiliang=Float
    jiangshuiqiangdu=VARCHAR
    qiwen=VARCHAR
    shidu=VARCHAR
    renkoumidu=Integer
    zhibeifugaidu=VARCHAR
    dizhigouzao=VARCHAR
    lishishanhongjilu=VARCHAR
    '''
    class Meta:
        db_table = 'zaihaixinxi'
        verbose_name = verbose_name_plural = '灾害信息'
class jinqixinxi(BaseModel):
    __doc__ = u'''jinqixinxi'''
    __tablename__ = 'jinqixinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jilushijian=models.DateField   (  null=True, unique=False, verbose_name='记录时间' )
    shengfen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='省份' )
    chengshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='城市' )
    juqu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='具区' )
    jingdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='经度' )
    weidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='纬度' )
    quyubianma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='区域编码' )
    jiangshuiliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='降水量(mm)' )
    jiangshuiqiangdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='降水强度(mm/h)' )
    qiwen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='气温(℃)' )
    shidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='湿度(%)' )
    renkoumidu=models.IntegerField  (  null=True, unique=False, verbose_name='人口密度(人/km²)' )
    zhibeifugaidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='植被覆盖度(%)' )
    dizhigouzao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地质构造' )
    lishishanhongjilu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='历史山洪记录' )
    '''
    jilushijian=Date
    shengfen=VARCHAR
    chengshi=VARCHAR
    juqu=VARCHAR
    jingdu=VARCHAR
    weidu=VARCHAR
    quyubianma=VARCHAR
    jiangshuiliang=VARCHAR
    jiangshuiqiangdu=VARCHAR
    qiwen=VARCHAR
    shidu=VARCHAR
    renkoumidu=Integer
    zhibeifugaidu=VARCHAR
    dizhigouzao=VARCHAR
    lishishanhongjilu=VARCHAR
    '''
    class Meta:
        db_table = 'jinqixinxi'
        verbose_name = verbose_name_plural = '近期信息'
class wangnianxinxi(BaseModel):
    __doc__ = u'''wangnianxinxi'''
    __tablename__ = 'wangnianxinxi'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jilushijian=models.DateField   (  null=True, unique=False, verbose_name='记录时间' )
    shengfen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='省份' )
    chengshi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='城市' )
    juqu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='具区' )
    jingdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='经度' )
    weidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='纬度' )
    quyubianma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='区域编码' )
    jiangshuiliang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='降水量(mm)' )
    jiangshuiqiangdu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='降水强度(mm/h)' )
    qiwen=models.CharField ( max_length=255, null=True, unique=False, verbose_name='气温(℃)' )
    shidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='湿度(%)' )
    renkoumidu=models.IntegerField  (  null=True, unique=False, verbose_name='人口密度(人/km²)' )
    zhibeifugaidu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='植被覆盖度(%)' )
    dizhigouzao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='地质构造' )
    lishishanhongjilu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='历史山洪记录' )
    '''
    jilushijian=Date
    shengfen=VARCHAR
    chengshi=VARCHAR
    juqu=VARCHAR
    jingdu=VARCHAR
    weidu=VARCHAR
    quyubianma=VARCHAR
    jiangshuiliang=VARCHAR
    jiangshuiqiangdu=VARCHAR
    qiwen=VARCHAR
    shidu=VARCHAR
    renkoumidu=Integer
    zhibeifugaidu=VARCHAR
    dizhigouzao=VARCHAR
    lishishanhongjilu=VARCHAR
    '''
    class Meta:
        db_table = 'wangnianxinxi'
        verbose_name = verbose_name_plural = '往年信息'
class newstype(BaseModel):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    typename=models.CharField ( max_length=255,null=False, unique=False, verbose_name='分类名称' )
    '''
    typename=VARCHAR
    '''
    class Meta:
        db_table = 'newstype'
        verbose_name = verbose_name_plural = '通知公告分类'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    __thumbsUp__='是'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='是'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='是'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    typename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='分类名称' )
    name=models.CharField ( max_length=255, null=True, unique=False, verbose_name='发布人' )
    headportrait=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    clicknum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='点击次数' )
    clicktime=models.DateTimeField  (auto_now=True,  null=True, unique=False, verbose_name='最近点击时间' )
    thumbsupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='赞' )
    crazilynum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='踩' )
    storeupnum=models.IntegerField  (  null=True, unique=False,default='0', verbose_name='收藏数' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    typename=VARCHAR
    name=VARCHAR
    headportrait=Text
    clicknum=Integer
    clicktime=DateTime
    thumbsupnum=Integer
    crazilynum=Integer
    storeupnum=Integer
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '通知公告'
class storeup(BaseModel):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'#后台列表权限
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='用户id' )
    refid=models.BigIntegerField  (  null=True, unique=False, verbose_name='商品id' )
    tablename=models.CharField ( max_length=255, null=True, unique=False, verbose_name='表名' )
    name=models.CharField ( max_length=255,null=False, unique=False, verbose_name='名称' )
    picture=models.TextField   (  null=True, unique=False, verbose_name='图片' )
    type=models.CharField ( max_length=255, null=True, unique=False,default='1', verbose_name='类型' )
    inteltype=models.CharField ( max_length=255, null=True, unique=False, verbose_name='推荐类型' )
    remark=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    userid=BigInteger
    refid=BigInteger
    tablename=VARCHAR
    name=VARCHAR
    picture=Text
    type=VARCHAR
    inteltype=VARCHAR
    remark=VARCHAR
    '''
    class Meta:
        db_table = 'storeup'
        verbose_name = verbose_name_plural = '收藏表'
class messages(BaseModel):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'#表属性hasMessage为是，新增留言板表messages,字段content（内容），userid（用户id）
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='留言人id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    avatarurl=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    content=models.TextField   ( null=False, unique=False, verbose_name='留言内容' )
    cpicture=models.TextField   (  null=True, unique=False, verbose_name='留言图片' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    rpicture=models.TextField   (  null=True, unique=False, verbose_name='回复图片' )
    '''
    userid=BigInteger
    username=VARCHAR
    avatarurl=Text
    content=Text
    cpicture=Text
    reply=Text
    rpicture=Text
    '''
    class Meta:
        db_table = 'messages'
        verbose_name = verbose_name_plural = '留言反馈'
