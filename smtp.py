import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
def sendmail(subject,txt):
    mail_host="192.168.x.x"  #设置服务器
     
     
    sender = 'wangqiang1988@github.com'  #设置发件人
    receivers = ['wangqiang1988@github.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
     
    message = MIMEText(f'{txt}', 'plain', 'utf-8')
    message['From'] = Header("邮件主题", 'utf-8')
    message['To'] =  Header("收件人名称", 'utf-8')
     
    subject = f'{subject}'
    message['Subject'] = Header(subject, 'utf-8')
     
     
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        #我这里使用的是非认证密码，用于自建邮箱发邮件，带密码的可自行更改这部分
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")

