#coding:utf-8
import base64, copy, logging, os, sys, time, xlrd, json, datetime, configparser
from django.http import JsonResponse
from django.apps import apps
import numbers
from django.db.models.aggregates import Count,Sum
from django.db.models import Case, When, IntegerField, F
from django.forms import model_to_dict
import requests
from util.CustomJSONEncoder import CustomJsonEncoder
from .models import zaihaixinxi
from util.codes import *
from util.auth import Auth
from util.common import Common
import util.message as mes
from django.db import connection
import random
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.db.models import Q
from util.baidubce_api import BaiDuBce
from .config_model import config
import pandas as pd


def zaihaixinxi_register(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")


        error = zaihaixinxi.createbyreq(zaihaixinxi, zaihaixinxi, req_dict)
        if error is Exception or (type(error) is str and "Exception" in error):
            msg['code'] = crud_error_code
            msg['msg'] = "用户已存在,请勿重复注册!"
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_login(request):
    if request.method in ["POST", "GET"]:
        msg = {'code': normal_code, "msg": mes.normal_code}
        req_dict = request.session.get("req_dict")
        datas = zaihaixinxi.getbyparams(zaihaixinxi, zaihaixinxi, req_dict)
        if not datas:
            msg['code'] = password_error_code
            msg['msg'] = mes.password_error_code
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        try:
            __sfsh__= zaihaixinxi.__sfsh__
        except:
            __sfsh__=None

        if  __sfsh__=='是':
            if datas[0].get('sfsh')!='是':
                msg['code']=other_code
                msg['msg'] = "账号已锁定，请联系管理员审核!"
                return JsonResponse(msg, encoder=CustomJsonEncoder)

        req_dict['id'] = datas[0].get('id')


        return Auth.authenticate(Auth, zaihaixinxi, req_dict)


def zaihaixinxi_logout(request):
    if request.method in ["POST", "GET"]:
        msg = {
            "msg": "登出成功",
            "code": 0
        }

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def zaihaixinxi_resetPass(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}

        req_dict = request.session.get("req_dict")

        columns=  zaihaixinxi.getallcolumn( zaihaixinxi, zaihaixinxi)

        try:
            __loginUserColumn__= zaihaixinxi.__loginUserColumn__
        except:
            __loginUserColumn__=None
        username=req_dict.get(list(req_dict.keys())[0])
        if __loginUserColumn__:
            username_str=__loginUserColumn__
        else:
            username_str=username
        if 'mima' in columns:
            password_str='mima'
        else:
            password_str='password'

        init_pwd = '123456'
        recordsParam = {}
        recordsParam[username_str] = req_dict.get("username")
        records=zaihaixinxi.getbyparams(zaihaixinxi, zaihaixinxi, recordsParam)
        if len(records)<1:
            msg['code'] = 400
            msg['msg'] = '用户不存在'
            return JsonResponse(msg, encoder=CustomJsonEncoder)

        eval('''zaihaixinxi.objects.filter({}='{}').update({}='{}')'''.format(username_str,username,password_str,init_pwd))

        return JsonResponse(msg, encoder=CustomJsonEncoder)



def zaihaixinxi_session(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}

        req_dict={"id":request.session.get('params').get("id")}
        msg['data']  = zaihaixinxi.getbyparams(zaihaixinxi, zaihaixinxi, req_dict)[0]

        return JsonResponse(msg, encoder=CustomJsonEncoder)


def zaihaixinxi_default(request):

    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code,"msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        req_dict.update({"isdefault":"是"})
        data=zaihaixinxi.getbyparams(zaihaixinxi, zaihaixinxi, req_dict)
        if len(data)>0:
            msg['data']  = data[0]
        else:
            msg['data']  = {}
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_page(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")

        global zaihaixinxi
        #当前登录用户信息
        tablename = request.session.get("tablename")

        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  =zaihaixinxi.page(zaihaixinxi, zaihaixinxi, req_dict, request)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_autoSort(request):
    '''

    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        if "clicknum"  in zaihaixinxi.getallcolumn(zaihaixinxi,zaihaixinxi):
            req_dict['sort']='clicknum'
        elif "browseduration"  in zaihaixinxi.getallcolumn(zaihaixinxi,zaihaixinxi):
            req_dict['sort']='browseduration'
        else:
            req_dict['sort']='clicktime'
        req_dict['order']='desc'
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = zaihaixinxi.page(zaihaixinxi,zaihaixinxi, req_dict)

        return JsonResponse(msg, encoder=CustomJsonEncoder)

#分类列表
def zaihaixinxi_lists(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":[]}
        msg['data'],_,_,_,_  = zaihaixinxi.page(zaihaixinxi, zaihaixinxi, {})
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_query(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        try:
            query_result = zaihaixinxi.objects.filter(**request.session.get("req_dict")).values()
            msg['data'] = query_result[0]
        except Exception as e:

            msg['code'] = crud_error_code
            msg['msg'] = f"发生错误：{e}"
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_list(request):
    '''
    前台分页
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code,  "data":{"currPage":1,"totalPage":1,"total":1,"pageSize":10,"list":[]}}
        req_dict = request.session.get("req_dict")
        #获取全部列名
        columns=  zaihaixinxi.getallcolumn( zaihaixinxi, zaihaixinxi)
        if "vipread" in req_dict and "vipread" not in columns:
          del req_dict["vipread"]
        #表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
        try:
            __foreEndList__=zaihaixinxi.__foreEndList__
        except:
            __foreEndList__=None
        try:
            __foreEndListAuth__=zaihaixinxi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        #authSeparate
        try:
            __authSeparate__=zaihaixinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __foreEndListAuth__ =="是" and __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and request.session.get("params") is not None:
                req_dict['userid']=request.session.get("params").get("id")

        tablename = request.session.get("tablename")
        if tablename == "users" and req_dict.get("userid") != None:#判断是否存在userid列名
            del req_dict["userid"]
        else:
            __isAdmin__ = None

            allModels = apps.get_app_config('main').get_models()
            for m in allModels:
                if m.__tablename__==tablename:

                    try:
                        __isAdmin__ = m.__isAdmin__
                    except:
                        __isAdmin__ = None
                    break

            if __isAdmin__ == "是":
                if req_dict.get("userid"):
                    # del req_dict["userid"]
                    pass
            else:
                #非管理员权限的表,判断当前表字段名是否有userid
                if "userid" in columns:
                    try:
                        pass
                    except:
                        pass
        #当列属性authTable有值(某个用户表)[该列的列名必须和该用户表的登陆字段名一致]，则对应的表有个隐藏属性authTable为”是”，那么该用户查看该表信息时，只能查看自己的
        try:
            __authTables__=zaihaixinxi.__authTables__
        except:
            __authTables__=None

        if __authTables__!=None and  __authTables__!={} and __foreEndListAuth__=="是":
            for authColumn,authTable in __authTables__.items():
                if authTable==tablename:
                    try:
                        del req_dict['userid']
                    except:
                        pass
                    params = request.session.get("params")
                    req_dict[authColumn]=params.get(authColumn)
                    username=params.get(authColumn)
                    break

        if zaihaixinxi.__tablename__[:7]=="discuss":
            try:
                del req_dict['userid']
            except:
                pass


        q = Q()
        msg['data']['list'], msg['data']['currPage'], msg['data']['totalPage'], msg['data']['total'], \
        msg['data']['pageSize']  = zaihaixinxi.page(zaihaixinxi, zaihaixinxi, req_dict, request, q)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_save(request):
    '''
    后台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys():
            del req_dict['clicktime']
        tablename=request.session.get("tablename")
        __isAdmin__ = None
        allModels = apps.get_app_config('main').get_models()
        for m in allModels:
            if m.__tablename__==tablename:

                try:
                    __isAdmin__ = m.__isAdmin__
                except:
                    __isAdmin__ = None
                break

        #获取全部列名
        columns=  zaihaixinxi.getallcolumn( zaihaixinxi, zaihaixinxi)
        if tablename!='users' and req_dict.get("userid")==None and 'userid' in columns  and __isAdmin__!='是':
            params=request.session.get("params")
            req_dict['userid']=params.get('id')


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']

        idOrErr= zaihaixinxi.createbyreq(zaihaixinxi,zaihaixinxi, req_dict)
        if idOrErr is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = idOrErr
        else:
            msg['data'] = idOrErr

        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_add(request):
    '''
    前台新增
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        tablename=request.session.get("tablename")

        #获取全部列名
        columns=  zaihaixinxi.getallcolumn( zaihaixinxi, zaihaixinxi)
        try:
            __authSeparate__=zaihaixinxi.__authSeparate__
        except:
            __authSeparate__=None

        if __authSeparate__=="是":
            tablename=request.session.get("tablename")
            if tablename!="users" and 'userid' in columns:
                try:
                    req_dict['userid']=request.session.get("params").get("id")
                except:
                    pass

        try:
            __foreEndListAuth__=zaihaixinxi.__foreEndListAuth__
        except:
            __foreEndListAuth__=None

        if __foreEndListAuth__ and __foreEndListAuth__!="否":
            tablename=request.session.get("tablename")
            if tablename!="users":
                req_dict['userid']=request.session.get("params").get("id")


        if 'addtime' in req_dict.keys():
            del req_dict['addtime']
        error= zaihaixinxi.createbyreq(zaihaixinxi,zaihaixinxi, req_dict)
        if error is Exception:
            msg['code'] = crud_error_code
            msg['msg'] = error
        else:
            msg['data'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_thumbsup(request,id_):
    '''
     点赞：表属性thumbsUp[是/否]，刷表新增thumbsupnum赞和crazilynum踩字段，
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        id_=int(id_)
        type_=int(req_dict.get("type",0))
        rets=zaihaixinxi.getbyid(zaihaixinxi,zaihaixinxi,id_)

        update_dict={
        "id":id_,
        }
        if type_==1:#赞
            update_dict["thumbsupnum"]=int(rets[0].get('thumbsupnum'))+1
        elif type_==2:#踩
            update_dict["crazilynum"]=int(rets[0].get('crazilynum'))+1
        error = zaihaixinxi.updatebyparams(zaihaixinxi,zaihaixinxi, update_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg, encoder=CustomJsonEncoder)


def zaihaixinxi_info(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data = zaihaixinxi.getbyid(zaihaixinxi,zaihaixinxi, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= zaihaixinxi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"  and  "clicknum"  in zaihaixinxi.getallcolumn(zaihaixinxi,zaihaixinxi):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}
            ret=zaihaixinxi.updatebyparams(zaihaixinxi,zaihaixinxi,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_detail(request,id_):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}

        data =zaihaixinxi.getbyid(zaihaixinxi,zaihaixinxi, int(id_))
        if len(data)>0:
            msg['data']=data[0]
            if msg['data'].__contains__("reversetime"):
                if isinstance(msg['data']['reversetime'], datetime.datetime):
                    msg['data']['reversetime'] = msg['data']['reversetime'].strftime("%Y-%m-%d %H:%M:%S")
                else:
                    if msg['data']['reversetime'] != None:
                        reversetime = datetime.datetime.strptime(msg['data']['reversetime'], '%Y-%m-%d %H:%M:%S')
                        msg['data']['reversetime'] = reversetime.strftime("%Y-%m-%d %H:%M:%S")

        #浏览点击次数
        try:
            __browseClick__= zaihaixinxi.__browseClick__
        except:
            __browseClick__=None

        if __browseClick__=="是"   and  "clicknum"  in zaihaixinxi.getallcolumn(zaihaixinxi,zaihaixinxi):
            try:
                clicknum=int(data[0].get("clicknum",0))+1
            except:
                clicknum=0+1
            click_dict={"id":int(id_),"clicknum":clicknum,"clicktime":datetime.datetime.now()}

            ret=zaihaixinxi.updatebyparams(zaihaixinxi,zaihaixinxi,click_dict)
            if ret!=None:
                msg['code'] = crud_error_code
                msg['msg'] = ret
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_update(request):
    '''
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")
        if 'clicktime' in req_dict.keys() and req_dict['clicktime']=="None":
            del req_dict['clicktime']
        if req_dict.get("mima") and "mima" not in zaihaixinxi.getallcolumn(zaihaixinxi,zaihaixinxi) :
            del req_dict["mima"]
        if req_dict.get("password") and "password" not in zaihaixinxi.getallcolumn(zaihaixinxi,zaihaixinxi) :
            del req_dict["password"]
        try:
            del req_dict["clicknum"]
        except:
            pass


        error = zaihaixinxi.updatebyparams(zaihaixinxi, zaihaixinxi, req_dict)
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error

        return JsonResponse(msg)


def zaihaixinxi_delete(request):
    '''
    批量删除
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code, "data": {}}
        req_dict = request.session.get("req_dict")

        error=zaihaixinxi.deletes(zaihaixinxi,
            zaihaixinxi,
             req_dict.get("ids")
        )
        if error!=None:
            msg['code'] = crud_error_code
            msg['msg'] = error
        return JsonResponse(msg)


def zaihaixinxi_vote(request,id_):
    '''
    浏览点击次数（表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1）
统计商品或新闻的点击次数；提供新闻的投票功能
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": mes.normal_code}


        data= zaihaixinxi.getbyid(zaihaixinxi, zaihaixinxi, int(id_))
        for i in data:
            votenum=i.get('votenum')
            if votenum!=None:
                params={"id":int(id_),"votenum":votenum+1}
                error=zaihaixinxi.updatebyparams(zaihaixinxi,zaihaixinxi,params)
                if error!=None:
                    msg['code'] = crud_error_code
                    msg['msg'] = error
        return JsonResponse(msg)

def zaihaixinxi_importExcel(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        excel_file = request.FILES.get("file", "")
        if excel_file.size > 100 * 1024 * 1024:  # 限制为 100MB
            msg['code'] = 400
            msg["msg"] = '文件大小不能超过100MB'
            return JsonResponse(msg)

        file_type = excel_file.name.split('.')[1]

        if file_type in ['xlsx', 'xls']:
            data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())
            table = data.sheets()[0]
            rows = table.nrows

            try:
                for row in range(1, rows):
                    row_values = table.row_values(row)
                    req_dict = {}
                    if str(row_values[0]) != '':
                        try:
                            date_tuple = xlrd.xldate_as_tuple(row_values[0], 0)
                            date_str = '-'.join([str(i) for i in date_tuple[:-3]])
                            req_dict['jilushijian'] = datetime.datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
                        except:
                            req_dict['jilushijian'] = row_values[0]
                    else:
                        req_dict['jilushijian'] = None
                    if '.0' in str(row_values[1]):
                        req_dict['shengfen'] = str(row_values[1]).split('.')[0]
                    elif str(row_values[1]) != '':
                        req_dict['shengfen'] = row_values[1]
                    else:
                        req_dict['shengfen'] = None
                    if '.0' in str(row_values[2]):
                        req_dict['chengshi'] = str(row_values[2]).split('.')[0]
                    elif str(row_values[2]) != '':
                        req_dict['chengshi'] = row_values[2]
                    else:
                        req_dict['chengshi'] = None
                    if '.0' in str(row_values[3]):
                        req_dict['juqu'] = str(row_values[3]).split('.')[0]
                    elif str(row_values[3]) != '':
                        req_dict['juqu'] = row_values[3]
                    else:
                        req_dict['juqu'] = None
                    if '.0' in str(row_values[4]):
                        req_dict['jingdu'] = str(row_values[4]).split('.')[0]
                    elif str(row_values[4]) != '':
                        req_dict['jingdu'] = row_values[4]
                    else:
                        req_dict['jingdu'] = None
                    if '.0' in str(row_values[5]):
                        req_dict['weidu'] = str(row_values[5]).split('.')[0]
                    elif str(row_values[5]) != '':
                        req_dict['weidu'] = row_values[5]
                    else:
                        req_dict['weidu'] = None
                    if '.0' in str(row_values[6]):
                        req_dict['quyubianma'] = str(row_values[6]).split('.')[0]
                    elif str(row_values[6]) != '':
                        req_dict['quyubianma'] = row_values[6]
                    else:
                        req_dict['quyubianma'] = None
                    if str(row_values[7]) != '':
                        req_dict['jiangshuiliang'] = float(row_values[7])
                    else:
                        req_dict['jiangshuiliang'] = None
                    if '.0' in str(row_values[8]):
                        req_dict['jiangshuiqiangdu'] = str(row_values[8]).split('.')[0]
                    elif str(row_values[8]) != '':
                        req_dict['jiangshuiqiangdu'] = row_values[8]
                    else:
                        req_dict['jiangshuiqiangdu'] = None
                    if '.0' in str(row_values[9]):
                        req_dict['qiwen'] = str(row_values[9]).split('.')[0]
                    elif str(row_values[9]) != '':
                        req_dict['qiwen'] = row_values[9]
                    else:
                        req_dict['qiwen'] = None
                    if '.0' in str(row_values[10]):
                        req_dict['shidu'] = str(row_values[10]).split('.')[0]
                    elif str(row_values[10]) != '':
                        req_dict['shidu'] = row_values[10]
                    else:
                        req_dict['shidu'] = None
                    if '.0' in str(row_values[11]):
                        req_dict['renkoumidu'] = str(row_values[11]).split('.')[0]
                    elif str(row_values[11]) != '':
                        req_dict['renkoumidu'] = row_values[11]
                    else:
                        req_dict['renkoumidu'] = None
                    if '.0' in str(row_values[12]):
                        req_dict['zhibeifugaidu'] = str(row_values[12]).split('.')[0]
                    elif str(row_values[12]) != '':
                        req_dict['zhibeifugaidu'] = row_values[12]
                    else:
                        req_dict['zhibeifugaidu'] = None
                    if '.0' in str(row_values[13]):
                        req_dict['dizhigouzao'] = str(row_values[13]).split('.')[0]
                    elif str(row_values[13]) != '':
                        req_dict['dizhigouzao'] = row_values[13]
                    else:
                        req_dict['dizhigouzao'] = None
                    if '.0' in str(row_values[14]):
                        req_dict['lishishanhongjilu'] = str(row_values[14]).split('.')[0]
                    elif str(row_values[14]) != '':
                        req_dict['lishishanhongjilu'] = row_values[14]
                    else:
                        req_dict['lishishanhongjilu'] = None
                    zaihaixinxi.createbyreq(zaihaixinxi, zaihaixinxi, req_dict)

            except:
                pass

        else:
            msg = {
                "msg": "文件类型错误",
                "code": 500
            }

        return JsonResponse(msg)

def zaihaixinxi_autoSort2(request):
    return JsonResponse({"code": 0, "msg": '',  "data":{}})



def zaihaixinxi_count(request):
    '''
    总数接口
    '''
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        req_dict = request.session.get("req_dict")
        where = ' where 1 = 1 '
        for key in req_dict:
            if req_dict[key] != None:
                where = where + " and key like '{0}'".format(req_dict[key])

        sql = "SELECT count(*) AS count FROM zaihaixinxi {0}".format(where)
        count = 0
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            count = online_dict['count']
        msg['data'] = count

        return JsonResponse(msg, encoder=CustomJsonEncoder)

# （按值统计）时间统计类型
def zaihaixinxi_value(request, xColumnName, yColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        where = ' where 1 = 1 '
        sql = ''
        if timeStatType == '日':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, ROUND(sum({1}),2) total FROM zaihaixinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, yColumnName, where, '%Y-%m-%d')

        if timeStatType == '月':
            sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, ROUND(sum({1}),2) total FROM zaihaixinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName, yColumnName, where, '%Y-%m')

        if timeStatType == '季':
            sql = "SELECT CONCAT(YEAR(MIN({0})), '-Q', QUARTER(MIN({0}))) AS {0}, SUM({1}) AS total FROM orders {2} GROUP BY YEAR({0}), QUARTER({0})".format(xColumnName, yColumnName, where)

        if timeStatType == '年':
            sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, ROUND(sum({1}),2) total FROM zaihaixinxi {2} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName, yColumnName, where, '%Y')

        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L
        req_dict = request.session.get("req_dict")
        if "order" in req_dict:
            order = req_dict["order"]
            if order == "desc":
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
            else:
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])

        if "limit" in req_dict and int(req_dict["limit"]) < len(L):
            msg['data'] = msg['data'][:int(req_dict["limit"])]
        return JsonResponse(msg, encoder=CustomJsonEncoder)

# 按值统计
def zaihaixinxi_o_value(request, xColumnName, yColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        where = ' where 1 = 1 '

        sql = "SELECT {0}, ROUND(sum({1}),2) AS total FROM zaihaixinxi {2} GROUP BY {0}".format(xColumnName, yColumnName, where)
        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L
        req_dict = request.session.get("req_dict")
        if "order" in req_dict:
            order = req_dict["order"]
            if order == "desc":
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
            else:
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])

        if "limit" in req_dict and int(req_dict["limit"]) < len(L):
            msg['data'] = msg['data'][:int(req_dict["limit"])]
        return JsonResponse(msg, encoder=CustomJsonEncoder)

# （按值统计）时间统计类型(多)
def zaihaixinxi_valueMul(request, xColumnName, timeStatType):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": []}

        req_dict = request.session.get("req_dict")

        where = ' where 1 = 1 '

        for item in req_dict['yColumnNameMul'].split(','):
            sql = ''
            if timeStatType == '日':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m-%d') {0}, ROUND(sum({1}),2) total FROM zaihaixinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m-%d')".format(xColumnName, item, where, '%Y-%m-%d')

            if timeStatType == '月':
                sql = "SELECT DATE_FORMAT({0}, '%Y-%m') {0}, ROUND(sum({1}),2) total FROM zaihaixinxi {2} GROUP BY DATE_FORMAT({0}, '%Y-%m')".format(xColumnName, item, where, '%Y-%m')

            if timeStatType == '季':
                sql = "SELECT CONCAT(YEAR(MIN({0})), '-Q', QUARTER(MIN({0}))) {0}, sum({1}) total FROM zaihaixinxi {2} GROUP BY YEAR({0}), QUARTER({0})".format(xColumnName, item, where)

            if timeStatType == '年':
                sql = "SELECT DATE_FORMAT({0}, '%Y') {0}, ROUND(sum({1}),2) total FROM zaihaixinxi {2} GROUP BY DATE_FORMAT({0}, '%Y')".format(xColumnName, item, where, '%Y')

            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'].append(L)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

# （按值统计(多)）
def zaihaixinxi_o_valueMul(request, xColumnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": []}

        req_dict = request.session.get("req_dict")
        where = ' where 1 = 1 '
        for item in req_dict['yColumnNameMul'].split(','):
            sql = "SELECT {0}, ROUND(sum({1}),2) AS total FROM zaihaixinxi {2} GROUP BY {0}".format(xColumnName, item, where)
            L = []
            cursor = connection.cursor()
            cursor.execute(sql)
            desc = cursor.description
            data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
            for online_dict in data_dict:
                for key in online_dict:
                    if 'datetime.datetime' in str(type(online_dict[key])):
                        online_dict[key] = online_dict[key].strftime(
                            "%Y-%m-%d %H:%M:%S")
                    else:
                        pass
                L.append(online_dict)
            msg['data'].append(L)
        return JsonResponse(msg, encoder=CustomJsonEncoder)

def zaihaixinxi_group(request, columnName):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}

        where = ' where 1 = 1 '
        sql = "SELECT COUNT(*) AS total, " + columnName + " FROM zaihaixinxi " + where + " GROUP BY " + columnName
        L = []
        cursor = connection.cursor()
        cursor.execute(sql)
        desc = cursor.description
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]
        for online_dict in data_dict:
            for key in online_dict:
                if 'datetime.datetime' in str(type(online_dict[key])):
                    online_dict[key] = online_dict[key].strftime("%Y-%m-%d")
                else:
                    pass
            L.append(online_dict)
        msg['data'] = L
        req_dict = request.session.get("req_dict")
        if "order" in req_dict:
            order = req_dict["order"]
            if order == "desc":
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'],reverse=True)
            else:
                msg['data'] = sorted((x for x in msg['data'] if x['total'] is not None),key=lambda x: x['total'])

        if "limit" in req_dict and int(req_dict["limit"]) < len(L):
            msg['data'] = msg['data'][:int(req_dict["limit"])]
        return JsonResponse(msg, encoder=CustomJsonEncoder)




import math

def zaihaixinxi_cleanse(request):
    if request.method in ["POST", "GET"]:
        msg = {"code": normal_code, "msg": "成功", "data": {}}
        try:
            list, _, _, total,_ = zaihaixinxi.page(zaihaixinxi, zaihaixinxi, {})
            df = pd.DataFrame(list)
            #随机填充
            df['jilushijian'].replace([None, ''], pd.NA,inplace = True)
            jilushijian_non_na = df['jilushijian'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'jilushijian']):
                    df.loc[i, 'jilushijian'] = jilushijian_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['shengfen'].replace([None, ''], pd.NA,inplace = True)
            shengfen_non_na = df['shengfen'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'shengfen']):
                    df.loc[i, 'shengfen'] = shengfen_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['chengshi'].replace([None, ''], pd.NA,inplace = True)
            chengshi_non_na = df['chengshi'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'chengshi']):
                    df.loc[i, 'chengshi'] = chengshi_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['juqu'].replace([None, ''], pd.NA,inplace = True)
            juqu_non_na = df['juqu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'juqu']):
                    df.loc[i, 'juqu'] = juqu_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['jingdu'].replace([None, ''], pd.NA,inplace = True)
            jingdu_non_na = df['jingdu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'jingdu']):
                    df.loc[i, 'jingdu'] = jingdu_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['weidu'].replace([None, ''], pd.NA,inplace = True)
            weidu_non_na = df['weidu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'weidu']):
                    df.loc[i, 'weidu'] = weidu_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['quyubianma'].replace([None, ''], pd.NA,inplace = True)
            quyubianma_non_na = df['quyubianma'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'quyubianma']):
                    df.loc[i, 'quyubianma'] = quyubianma_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['jiangshuiliang'].replace([None, ''], pd.NA,inplace = True)
            jiangshuiliang_non_na = df['jiangshuiliang'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'jiangshuiliang']):
                    df.loc[i, 'jiangshuiliang'] = jiangshuiliang_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['jiangshuiqiangdu'].replace([None, ''], pd.NA,inplace = True)
            jiangshuiqiangdu_non_na = df['jiangshuiqiangdu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'jiangshuiqiangdu']):
                    df.loc[i, 'jiangshuiqiangdu'] = jiangshuiqiangdu_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['qiwen'].replace([None, ''], pd.NA,inplace = True)
            qiwen_non_na = df['qiwen'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'qiwen']):
                    df.loc[i, 'qiwen'] = qiwen_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['shidu'].replace([None, ''], pd.NA,inplace = True)
            shidu_non_na = df['shidu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'shidu']):
                    df.loc[i, 'shidu'] = shidu_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['renkoumidu'].replace([None, ''], pd.NA,inplace = True)
            renkoumidu_non_na = df['renkoumidu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'renkoumidu']):
                    df.loc[i, 'renkoumidu'] = renkoumidu_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['zhibeifugaidu'].replace([None, ''], pd.NA,inplace = True)
            zhibeifugaidu_non_na = df['zhibeifugaidu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'zhibeifugaidu']):
                    df.loc[i, 'zhibeifugaidu'] = zhibeifugaidu_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['dizhigouzao'].replace([None, ''], pd.NA,inplace = True)
            dizhigouzao_non_na = df['dizhigouzao'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'dizhigouzao']):
                    df.loc[i, 'dizhigouzao'] = dizhigouzao_non_na.sample(n=1,replace=True).values[0]
            #随机填充
            df['lishishanhongjilu'].replace([None, ''], pd.NA,inplace = True)
            lishishanhongjilu_non_na = df['lishishanhongjilu'].dropna()  # 获取非空值
            for i in df.index:
                if pd.isna(df.loc[i, 'lishishanhongjilu']):
                    df.loc[i, 'lishishanhongjilu'] = lishishanhongjilu_non_na.sample(n=1,replace=True).values[0]
            data_list = df.to_dict(orient='records')
            zaihaixinxi.deletes(zaihaixinxi,zaihaixinxi,ids=[i["id"] for i in list])
            batchList = []
            for dl in data_list:
                filtered_data = {k: v for k, v in dl.items() if v not in [None, '', float('nan')] and (not isinstance(v, float) or not math.isnan(v))}
                batchList.append(zaihaixinxi(**filtered_data))
            zaihaixinxi.objects.bulk_create(batchList)
        except Exception as e:
            msg["code"] = other_code
            msg["msg"] = e.__str__()

        return JsonResponse(msg)





