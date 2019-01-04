##Blur
from PIL import Image
from PIL import ImageFilter

try:

	##Abrimos la imagen
	img = Image.open("chester.jpg")
	##Imprimimso el tamaño de la imagen
	print(img.size)

	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	blurred = img.filter(ImageFilter.BLUR)
	##Mostramos la nueva imagen
	blurred.show()
	##ALmacenamos la imagen afectada
	blurred.save("imgBlur.jpg")

except IOError:
	print("No se encontro tu imagen >:c")
