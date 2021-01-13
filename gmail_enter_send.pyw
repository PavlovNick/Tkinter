from tkinter import *
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import email
from platform import python_version

server = 'smtp.gmail.com'

root = Tk()
root.title("3 індіва")
root.resizable(width = False, height = False)

fn = ("Arial Greek", 12, "bold")
col1 = "#FFFFFF" 
col2 = "#000000"
col3 = "#FF0000"

b_padx = 12
b_pady = 5

T_aut = ["Авторизація", "Почта", "Пароль"]

#////////////////////////////////////FUNCTION////////////////////////////////////////#
def Send_message(event):
	user = E_mail.get()
	password = E_password.get()
	recipients = E_recipients_str.get()
	sender = user
	subject = E_subject_str.get()
	text = T_text.get(1.0, END)
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = 'Python script <' + sender + '>'
	msg['To'] = ', '.join(recipients)
	msg['Reply-To'] = sender
	msg['Return-Path'] = sender
	msg['X-Mailer'] = 'Python/'+(python_version())
	 
	part_text = MIMEText(text, 'plain')
	 
	msg.attach(part_text)

	mail = smtplib.SMTP_SSL(server)
	mail.login(user, password)
	mail.sendmail(sender, recipients, msg.as_string())
	mail.quit()

def Get_message(event):
	user = E_mail.get()
	password = E_password.get()
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(user, password)
	 
	mail.list()
	mail.select("inbox")

	result, data = mail.search(None, "ALL")
	 
	ids = data[0]
	id_list = ids.split()
	latest_email_id = id_list[-1]
	 
	result, data = mail.fetch(latest_email_id, "(RFC822)")
	raw_email = data[0][1]
	raw_email_string = raw_email.decode('utf-8')
	#print(raw_email_string)

	email_message = email.message_from_string(raw_email_string)
	L_from_['text'] = "від: " + str(email.utils.parseaddr(email_message['From']))
	L_date_['text'] = "дата: " + str(email_message['Date'])
	L_subject_['text'] = "тема: " + str(email_message['Subject'])

	if email_message.is_multipart():
	    for payload in email_message.get_payload():
	        body = payload.get_payload(decode=True).decode('utf-8')
	        L_message_['text'] = body
	        break
	else:    
	    body = payload.get_payload(decode=True).decode('utf-8')
	    L_message_['text'] = body

def Authorization(event):
	user = E_mail.get()
	password = E_password.get()
	mail = smtplib.SMTP_SSL(server)
	try:
		mail.login(user, password)
	except smtplib.SMTPAuthenticationError:
		print("Помилка при авторизації")
		L_error['text'] = "Помилка при авторизації"
		E_pass.delete(0, END)
	else:
		F_aut.destroy()
		F_email.pack()
#////////////////////////////////////FUNCTION////////////////////////////////////////#

#SMTPAuthenticationError
F_aut = Frame(root, bg=col1)
F_email = Frame(root, bg=col1)
F_send_mes = LabelFrame(F_email, text="Надіслати повідомлення", bg=col1)
F_get_mes = LabelFrame(F_email, text="Отримати повідомлення", bg=col1)

#\\\\\\\\\\\\\\\\\GET_MESSAGE\\\\\\\\\\\\\\\\\#
L_from_ = Label(F_get_mes, text = "" ,font=fn, fg=col2, bg=col1)
L_date_ = Label(F_get_mes, text = "" ,font=fn, fg=col2, bg=col1)
L_subject_ = Label(F_get_mes, text = "" ,font=fn, fg=col2, bg=col1)
L_message_ = Label(F_get_mes, text = "" ,font=fn, fg=col2, bg=col1)

B_get_mess = Button(F_get_mes, text="Отримати повідомлення", font=fn, fg=col1, bg=col3)
B_get_mess.bind('<Button-1>', Get_message)
#\\\\\\\\\\\\\\\\\GET_MESSAGE\\\\\\\\\\\\\\\\\#

#\\\\\\\\\\\\\\\\\SEND_MESSAGE\\\\\\\\\\\\\\\\\#

L_recipients = Label(F_send_mes, text = "Кому:" ,font=fn, fg=col2, bg=col1)
L_subject = Label(F_send_mes, text = "Тема:" ,font=fn, fg=col2, bg=col1)
L_text = Label(F_send_mes, text = "Повідомлення:" ,font=fn, fg=col2, bg=col1)

E_recipients_str = StringVar()
E_recipients = Entry(F_send_mes, textvariable=E_recipients_str, font=fn, bd=2)
E_subject_str = StringVar()
E_subject = Entry(F_send_mes, textvariable=E_subject_str, font=fn, bd=2)
T_text = Text(F_send_mes, width=40, height=5, font=fn)

B_send_mess = Button(F_send_mes, text="Надіслати повідомлення", font=fn, fg=col1, bg=col3)
B_send_mess.bind('<Button-1>', Send_message)
#\\\\\\\\\\\\\\\\\SEND_MESSAGE\\\\\\\\\\\\\\\\\#

#\\\\\\\\\\\\\\\\\Authentication\\\\\\\\\\\\\\\\\#
L_main_aut = Label(F_aut, text = T_aut[0] ,font=("Arial Greek", 14, "bold"), fg=col3, bg=col1)
L_email = Label(F_aut, text = T_aut[1] ,font=fn, fg=col2, bg=col1)
L_pass = Label(F_aut, text = T_aut[2] ,font=fn, fg=col2, bg=col1)
L_error = Label(F_aut, text = "" ,font=fn, fg=col3, bg=col1)

E_mail = StringVar()
E_password = StringVar()
E_E_mail = Entry(F_aut, textvariable=E_mail, font=fn, bd=2, width=30)
E_pass = Entry(F_aut, textvariable=E_password, font=fn, bd=2, width=30, show="*")

B_aut = Button(F_aut, text="Авторизуватись", font=fn, fg=col1, bg=col3)
B_aut.bind('<Button-1>', Authorization)
#\\\\\\\\\\\\\\\\\Authentication\\\\\\\\\\\\\\\\\#

F_aut.pack()
L_main_aut.pack(side=TOP, fill=BOTH, padx=b_padx, pady=b_pady)
L_email.pack(side=TOP, fill=BOTH, padx=b_padx, pady=b_pady)
E_E_mail.pack(side=TOP, fill=BOTH, padx=b_padx, pady=b_pady)
L_pass.pack(side=TOP, fill=BOTH, padx=b_padx, pady=b_pady)
E_pass.pack(side=TOP, fill=BOTH, padx=b_padx, pady=b_pady)
B_aut.pack(side=TOP, fill=BOTH, padx=b_padx, pady=b_pady)
L_error.pack(side=TOP, fill=BOTH)
#

F_send_mes.pack(side=LEFT, padx=10, pady=10)
L_recipients.pack(side=TOP, fill=BOTH, padx=b_padx)
E_recipients.pack(side=TOP, fill=BOTH, padx=b_padx)
L_subject.pack(side=TOP, fill=BOTH, padx=b_padx)
E_subject.pack(side=TOP, fill=BOTH, padx=b_padx)
L_text.pack(side=TOP, fill=BOTH, padx=b_padx)
T_text.pack(side=TOP, fill=BOTH, padx=b_padx)
B_send_mess.pack(side=TOP, fill=BOTH, padx=b_padx)

F_get_mes.pack(side=LEFT, padx=10, pady=10, fill=BOTH)
L_from_.pack(side=TOP, fill=BOTH, padx=b_padx)
L_date_.pack(side=TOP, fill=BOTH, padx=b_padx)
L_subject_.pack(side=TOP, fill=BOTH, padx=b_padx)
L_message_.pack(side=TOP, fill=BOTH, padx=b_padx, pady=b_pady)
B_get_mess.pack(side=BOTTOM, fill=BOTH, padx=b_padx, )

root.mainloop()