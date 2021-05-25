import smtplib
from email.message import EmailMessage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['Subject'] = 'Training Invitation HI'
msg['From'] = 'Mukesh Training Team'
msg['To'] = 'hanshengliang@outlook.com'

body = "<h1>HELLO</h1>"
msgText = MIMEText('<b>%s</b>' % (body), 'html')
msg.attach(msgText)

# Text File
# filename = "test.txt"
# msg.attach(MIMEText(open(filename).read()))

# PDF
filename = "1.pdf"
with open(filename, "rb") as f:
    attach = MIMEApplication(f.read(), _subtype="pdf")
attach.add_header('Content-Disposition','attachment',filename=str(filename))
msg.attach(attach)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("hanshengliang0286@gmail.com", "hansheng000512081415")

server.send_message(msg)
server.quit()
