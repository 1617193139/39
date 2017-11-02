import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = '17766472625@163.com'
msg['to'] = '1332553880@qq.com'
msg['subject'] = 'Lazy'
content = "So lazy"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('17766472625@163.com', 'zzc123456')
smtp.sendmail('17766472625@163.com', '1332553880@qq.com', str(msg))
smtp.quit()

