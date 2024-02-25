#Importar bibliotecas necesarias
import cv2
#Usa el nombre correcto de la imagen
img = cv2.imread("g-mihalcea.png")
f, c , _ = img.shape
porcentaje = 50
columnas = (c*porcentaje)//100
filas = (f*porcentaje)//100
#imgR = cv2.resize(img, (columnas, filas))

imgR = cv2.resize(img,None, fx = 1.5, fy=1.5)

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Redimensionada", imgR)
#cv2.imwrite("lechuga50.png", imgR)
cv2.waitKey(0)
cv2.destroyAllWindows()
