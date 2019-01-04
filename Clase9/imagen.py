##Procesamiento de imagenes

##importamos Image desde PIL
from PIL import Image
from PIL import ImageFilter

##Utilizar excepciones try
try:
	##Creamos un objeto que almacene la imagen para poder manipularla
	img = Image.open("imagenes/chester.jpg")

	##modo de una imagen
	#print(img.mode)
	##determinado pixel
	#print(img.getpixel((100,200)))

	##Convertir la imagen a un modo determinado
	#img = img.convert("L")

	##Rotar imagen
	##Si queremos que se vea completamente utilizamos expand
	#img = img.rotate(20, expand = True)

	##Opcion B de rotamiento
	#img = img.transpose(Image.ROTATE_180)


	##ESCALAR una imagen
	#1° obtenemos el tamaño de la imagen
	print(img.size)

	#2° reasignamos el tamaño
	#ancho = int(img.width/2)
	#altura = int(img.height/2)
	#img = img.resize((ancho, altura))


	##CORTAR IMAGENES
	#definimos los pixeles que cortaremos
	#box =  (100, 100, 300, 200)
	#img = img.crop(box)


	##MONTAJE DE IMAGENES
	#copy = img.resize((100, 100))
	#Definimos que vamos a pegar y le definimos la posicion
	#img.paste(copy, ((100,100)))


	##FILTROS
	blurred = img.filter(ImageFilter.BLUR)

	blurred = blurred.filter(ImageFilter.BLUR)

	blurred.show()

	##Guardamos la imagen en una direccion determinada
	blurred.save("imagenes/news/imgBlur.jpg")

	##Desplegamos la imagen
	#img.show()

except IOError:
	print("No se encontro tu imagen >:c")
