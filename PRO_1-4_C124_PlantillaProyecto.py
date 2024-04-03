# Para capturar el fotograma
import cv2

# Para procesar la arreglo de la imagen
import numpy as np


# Importar el módulo tensorflow y cargar el modelo



# Adjuntando el índice de la cámara como 0 con la aplicación del software
camera = cv2.VideoCapture(0)

# Bucle infinito
while True:

	# Leyendo/Solicitando un fotograma de la cámara
	status , frame = camera.read()

	# Si somos capaces de leer exitosamente el fotograma
	if status:

		# Voltear la imagen
		frame = cv2.flip(frame , 1)
		
		
		
		# Redimensionar el fotograma
		
		# Expandir las dimensiones 
		
		# Normalizar antes de alimentar al modelo
		
		# Obtener predicciones del modelo
		
		
		
		# Mostrando los fotogramas capturados
		cv2.imshow('Alimentar' , frame)

		# Esperando 1ms
		code = cv2.waitKey(1)
		
		# Si se preciona la barra espaciadora, romper el bucle
		if code == 32:
			break

# Liberar la cámara de la aplicación del software
camera.release()

# Cerrar la ventana abierta
cv2.destroyAllWindows()
