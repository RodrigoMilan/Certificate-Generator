from PIL import Image, ImageDraw, ImageFont
from email.message import EmailMessage
import pandas as pd
import smtplib
import imghdr

def main(gmail_user, gmail_pass, excel, certificate, messsageValue, messageText, subjectValue, subjectText):

	df = pd.read_excel(excel)

	name_list = df['Name'].to_list()
	email_list = df['e-mail'].to_list()

	for i in range(len(name_list)):
		im = Image.open(certificate)
		d = ImageDraw.Draw(im)
		location = (72,280)
		text_color = (0,0,0)
		try:
			font = ImageFont.truetype("Arial.TTF", 20)
		except:
			font = ImageFont.truetype("arial.ttf", 20)

		d.text(location,name_list[i],fill=text_color,font=font)
		im.save("certificate_"+name_list[i]+".pdf")

		msg = EmailMessage()
		if subjectValue == 1:
			msg['Subject'] = subjectText
		elif subjectValue == 0:
			msg['Subject'] = 'Certificate'
		msg['From'] = gmail_user
		msg['To'] = email_list[i]
		with open("certificate_"+name_list[i]+".pdf",'rb') as fp_file:
			fp = fp_file.read()
		msg.add_attachment(fp, maintype='application',subtype='pdf',filename='certificate.pdf')

		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user,gmail_pass)
		server.send_message(msg)
		server.close()
