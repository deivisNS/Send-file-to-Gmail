import yagmail 	#para conectar y enviar mensajes pos gmail
import os
from users_and_files import *	#modulo que busca los archivos y correos



#usuario de gmail
user_gmail = "UserMail@gmail.com"

#contraseña de aplicacion
password_gmail = "AppPassword"

#nos conectamos con gmail
yag = yagmail.SMTP(user = user_gmail, password = password_gmail)	 



def send_mail(dest, subject, message, sending_files):

	try:

		#enviamos el mensaje
		yag.send(
			dest, #destinatario
			subject, #asunto del mensaje
			message, #cuerpo del mensaje
			attachments = sending_files	#archivo a enviar
			)

		return "Sent.\n"


	except:

		return "Could not send.\n"	 
			


#errors > lista con las carpetas que no tienen el archivo gmail.txt o sin correo. users > diccionario con la direccion de correo y archivos a enviar
errors, users = files()	#funcion del modulo users_and_files	
print(errors, users)

#cuantas carpetas hay en companies
directories = os.listdir("companies")


#recorremos las direcciones de correo y archivos a enviar de cada direccion	
for mail, sending in users.items():

	#recorremos los archivos a enviar
	for file in sending:
		
		#recorremos las carpetas que hay en companies
		for company in directories:
			
			#confirmamos uno a uno si el archivo a enviar se encuentra en la carpeta correspondiente	
			if os.path.exists(f"companies/{company}/{file}"):

				#extraemos el binario del archivo
				file_type = open(f"companies/{company}/{file}", "rb")
				print(f"Sending: {file}\nTo: {mail}")
				
				#y enviamos la informacion a la funcion que enviara el mensaje
				print(send_mail(mail, "Message", "Files to Send.", file_type))
			
				break