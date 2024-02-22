import cv2

img = cv2.imread("gabriel-mihalcea.png")
f, c , _ = img.shape
porcentaje = 50
columnas = (c*porcentaje)//100
filas = (f*porcentaje)//100
imgR = cv2.resize(img, (columnas, filas))

cv2.imshow("Imagen Original", img)
cv2.imshow("Imagen Redimensionada", imgR)
cv2.imwrite("lechuga50.png", imgR)
cv2.waitKey(0)
cv2.destroyAllWindows()
