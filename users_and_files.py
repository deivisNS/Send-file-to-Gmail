import os
import pickle




def files(send_repeat = False):	#send_repeat es si queremos que se envien archivos ya enviados con anterioridad

	old_sends = []

	files_sends = []

	errors = []

	users = {}


	#buscamos cuantas carpetas de empresas hay
	directories = os.listdir("companies")


	for directory in directories:
		
		#preguntamos si el archivo txt con la direccion de correo existe
		if os.path.exists(f"companies/{directory}/gmail.txt"):

			#buscamos los archivos a enviar 
			to_send = os.listdir(f"companies/{directory}")

			
			#extramos y guardamos el correo que se encuentra en el archivo txt
			with open(f"companies/{directory}/gmail.txt", "r") as txt:

				gmail = txt.read()


			#comprobamos si hay una direccion de correo
			if gmail != "":

				#preguntamos si el archivo pickle que contiene los nombre de los archivos ya enviados anteriormente existe
				if os.path.exists(f"companies/{directory}/enviados.pickle"):

					#extraemos los datos del archivo pickle
					with open(f"companies/{directory}/enviados.pickle", "rb") as file:

						old_sends = pickle.load(file)


				else:

					#si no existe el archivo pickle lo creamos
					with open(f"companies/{directory}/enviados.pickle", "wb") as file:

						pickle.dump(old_sends, file)


				#recorremos los archivos a enviar 
				for file in to_send:
					
					#excuimos los archivos txt y pickle
					if not file.endswith(".txt") and not file.endswith(".pickle"):

						#agregamos todos los archivos sin importar si ya fueron enviados anteriormente
						if send_repeat == True:
							
							files_sends.append(file)


						#si no queremos que se repitan envios antiguos
						else:

							#agregamos solo los archivos que no han sido enviados anteriormente
							if not file in old_sends:
								
								files_sends.append(file)


				#unimos y guardamos los nuevos archivos enviados junto a los antiguos
				with open(f"companies/{directory}/enviados.pickle", "wb") as file:

					pickle.dump(old_sends + files_sends, file)


				#diccionario con la llave siendo el correo y los valores siendo una lista con los archivos a enviar a ese correo
				users[gmail] = files_sends

				files_sends = []

				old_sends = []


			else:

				#si el archivo txt no tiene contenido alguno
				errors.append(f"The gmail file in {directory} exist, but it has no content.")


		else:

			#si no existe el archivo txt lo informamos
			errors.append(f"The gmail file is not in {directory}.")


	#enviamos el informe de errores y el  diccionario con la direccion de correo y los archivos a enviar
	return (errors, users)

