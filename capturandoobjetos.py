import cv2 #imagem
import numpy as np #numeros
import imutils #funções auxiliares
import os #preparações do sistema

#verifica pasta
Datos = 'n'
if not os.path.exists(Datos):
	print('Carpeta creada: ', Datos)
	os.makedirs(Datos)

#abre conexão com a camera
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#coordenadas definidas
x1, y1 = 190, 80
x2, y2 = 450, 398

#captura continua
count = 0
while True:

	ret, frame = cap.read()
	if ret == False:  break

#copia do frame	
	imAux = frame.copy()
	cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

	#recorta regiao
	objeto = imAux[y1:y2,x1:x2]
	objeto = imutils.resize(objeto, width=38)
	# print(objeto.shape)

#salva frame na pasta
	k = cv2.waitKey(1)
	if k == ord('s'):
		cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
		print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
		count = count + 1

#sai do loop
	if k == 27: 
		break

#mostra duas janelas com os frames
	cv2.imshow('frame',frame)
	cv2.imshow('objeto',objeto)

#fecham todas as janelas e interrompe opencv
cap.release()
cv2.destroyAllWindows()