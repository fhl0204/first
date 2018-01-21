#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import sys
import os
from datetime import *
#
def send_mail(to_list, sub):
        me = mail_user
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ",".join(to_list)
#创造数据
        #a=os.popen("bash /data/sh/md_sla.sh").read().strip('\n').split(',')
        a = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']

        #构造html
        d = datetime.now()
        dt = d.strftime('%Y-%m-%d %H:%M:%S')
        at = (d - timedelta(1)).strftime('%Y-%m-%d %H:%M:%S')
        timezone  = at + ' ~ ' + dt
#构造html
        html = """\
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>萌店AB环境</title>
<body>
<div id="container">
  <p><strong>萌店sla状态统计</strong></p>
  <p>采集时间: """ + timezone + """</p>
  <div id="content">
   <table width="500" border="2" bordercolor="red" cellspacing="2">
  <tr>
    <td><strong>站点</strong></td>
    <td><strong>总访问量</strong></td>
    <td><strong>正常数</strong></td>
    <td><strong>正常百分比</strong></td>
    <td><strong>异常数</strong></td>
    <td><strong>异常百分比</strong></td>
  </tr>
  <tr>
    <td><a href="http://log.xxx.com/#/dashboard/file/node.json">node</a></td>
    <td>""" + a[4] + """</td>
    <td>""" + a[0] + """</td>
    <td>""" + a[1] + """</td>
    <td>""" + a[2] + """</td>
    <td>""" + a[3] + """</td>
  </tr>
  <tr>
    <td><a href="http://log.xxxlcom/#/dashboard/file/api.json">api</a></td>
    <td>""" + a[9] + """</td>
    <td>""" + a[5] + """</td>
    <td>""" + a[6] + """</td>
    <td>""" + a[7] + """</td>
    <td>""" + a[8] + """</td>
  </tr>
  <tr>
    <td><a href="http://log.xxx.com/#/dashboard/file/mapi.json">mapi</a></td>
    <td>""" + a[14] + """</td>
    <td>""" + a[10] + """</td>
    <td>""" + a[11] + """</td>
    <td>""" + a[12] + """</td>
    <td>""" + a[13] + """</td>
  </tr>
  <tr>
    <td><a href="http://log.xxx.com/#/dashboard/file/yunying-sla.json">yunying</a></td>
    <td>""" + a[19] + """</td>
    <td>""" + a[15] + """</td>
    <td>""" + a[16] + """</td>
    <td>""" + a[17] + """</td>
    <td>""" + a[18] + """</td>
  </tr>
</table>
  </div>
</div>
<p><strong>点击站点名可查看详细表图</strong> </p>
</div>
</body>
</html>
        """
        context = MIMEText(html,_subtype='html',_charset='utf-8')  #解决乱码
        msg.attach(context)
        try:
                send_smtp = smtplib.SMTP()
                send_smtp.connect(mail_host)
                send_smtp.login(mail_user, mail_pass)
                send_smtp.sendmail(me, to_list, msg.as_string())
                send_smtp.close()
                return True
        except Exception, e:
                print str(e)
                return False
if __name__ == '__main__':
    # 设置服务器名称、用户名、密码以及邮件后缀
    mail_host = 'mail.163.com'
    mail_user = '17317671651@163.com'
    mail_pass = '0204fhl'
    #mailto_lists = sys.argv[1]
    #mailto_list = mailto_lists.split(',')   #发送多人
    #sub= sys.argv[2]
    mailto_list = ['1390671039@qq.com',]
    sub= "状态sla"
    #send_mail(mailto_list, sub)
    if send_mail(mailto_list, sub):
        print "Send mail succed!"
    else:
        print "Send mail failed!"
'''  # another example


import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

filename='/home/qinwt/PycharmProjects/first/reptile/result.csv' #附件地址

def send_mail(to_list,sub,context,filename):  #to_list：收件人；sub：主题；content：邮件内容
    mail_host="smtp.163.com"  #设置服务器
    mail_user="17317671651@163.com"    #用户名
    mail_pass="0204fhl"   #口令
    mail_postfix="163.com"  #发件箱的后缀
    me="服务器"+"<"+mail_user+"@"+mail_postfix+">"   #这里的“服务器”可以任意设置，收到信后，将按照设置显示
    msg = MIMEMultipart() #给定msg类型
    msg['Subject'] = sub #邮件主题
    msg['From'] = me
    msg['To'] = ";".join(mailto_list)
    msg.attach(context)
    #构造附件1
    att1 = MIMEText(open(filename, 'rb').read(), 'xls', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename='+filename[-6:]#这里的filename可以任意写，写什么名字，邮件中显示什么名字，filename[-6:]指的是之前附件地址的后6位
    msg.attach(att1)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception as e:
        print e
        return False


if __name__ == '__main__':
    mailto_list=["1390671039@qq.com"]
    a=pd.DataFrame({'数列1':(1,1,1,1),'数列2':(2,2,2,2),'数列3':(3,3,3,3),'数列4':(4,4,4,4)})
    a.index={'行1','行2','行3','行4'} #这里dataframe类型a就是要输出的表格
    sub="hahaha"
    d='' #表格内容
    for i in range(len(a)):
        d=d+"""
        <tr>
          <td>""" + str(a.index[i]) + """</td>
          <td>""" + str(a.iloc[i][0]) + """</td>
          <td width="60" align="center">""" + str(a.iloc[i][1]) + """</td>
          <td width="75">""" + str(a.iloc[i][2]) + """</td>
          <td width="80">""" + str(a.iloc[i][3]) + """</td>
        </tr>"""
    html = """\
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />


<body>
<div id="container">
<p><strong>测试程序邮件发送:</strong></p>
<div id="content">
 <table width="30%" border="2" bordercolor="black" cellspacing="0" cellpadding="0">
<tr>
  <td width="40"><strong>统计</strong></td>
  <td width="50"><strong>数列1</strong></td>
  <td width="60" align="center"><strong>数列2</strong></td>
  <td width="50"><strong>数列3</strong></td>
  <td width="80"><strong>数列4</strong></td>
</tr>"""+d+"""
</table>
</div>
</div>
</div>
</body>
</html>
      """
    context = MIMEText(html,_subtype='html',_charset='utf-8')  #解决乱码
    if send_mail(mailto_list,sub,context,filename):
        print ("发送成功")
    else:

        print ("发送失败")

