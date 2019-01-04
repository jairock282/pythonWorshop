##Blur
from PIL import Image
from PIL import ImageFilter

##FILTRO BLUR
def blurred(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	blurred = self.filter(ImageFilter.BLUR)
	##Mostramos la nueva imagen
	blurred.show()
	##ALmacenamos la imagen afectada
	blurred.save("news/imgBlur.jpg")

##FILTRO CONTOUR
def contour(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	contoured = self.filter(ImageFilter.CONTOUR)
	##Mostramos la nueva imagen
	contoured.show()
	##ALmacenamos la imagen afectada
	contoured.save("news/imgContour.jpg")

##FILTRO DETAIL
def detail(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	detailed = self.filter(ImageFilter.DETAIL)
	##Mostramos la nueva imagen
	detailed.show()
	##ALmacenamos la imagen afectada
	detailed.save("news/imgDetail.jpg")

##FILTRO EDGE_ENHANCE
def edge_enhance(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	eenhance = self.filter(ImageFilter.EDGE_ENHANCE)
	##Mostramos la nueva imagen
	eenhance.show()
	##ALmacenamos la imagen afectada
	eenhance.save("news/imgEenhance.jpg")

##FILTRO EDGE_ENHANCE_MORE
def edge_enhance_more(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	eenhanceMORE = self.filter(ImageFilter.EDGE_ENHANCE_MORE)
	##Mostramos la nueva imagen
	eenhanceMORE.show()
	##ALmacenamos la imagen afectada
	eenhanceMORE.save("news/imgEenhanceMore.jpg")

##FILTRO EMBOSS
def emboss(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	emboss = self.filter(ImageFilter.EMBOSS)
	##Mostramos la nueva imagen
	emboss.show()
	##ALmacenamos la imagen afectada
	emboss.save("news/imgEmboss.jpg")

##FILTRO FIND_EDGES
def find_edges(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	fEdges = self.filter(ImageFilter.FIND_EDGES)
	##Mostramos la nueva imagen
	fEdges.show()
	##ALmacenamos la imagen afectada
	fEdges.save("news/imgFEdges.jpg")

##FILTRO SMOOTH
def smooth(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	smooth = self.filter(ImageFilter.SMOOTH)
	##Mostramos la nueva imagen
	smooth.show()
	##ALmacenamos la imagen afectada
	smooth.save("news/imgSmooth.jpg")

##FILTRO SMOOTH_MORE
def smoothMore(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	smoothMore = self.filter(ImageFilter.SMOOTH_MORE)
	##Mostramos la nueva imagen
	smoothMore.show()
	##ALmacenamos la imagen afectada
	smoothMore.save("news/imgSmoothMore.jpg")

##FILTRO SHARPEN
def sharpen(self):

	print("Llamando funcion")
	##Aplicamos el filtro BLUR y almacenamos en un nuevo objeto
	sharpen = self.filter(ImageFilter.SHARPEN)
	##Mostramos la nueva imagen
	sharpen.show()
	##ALmacenamos la imagen afectada
	sharpen.save("news/imgSharpen.jpg")

##Diccionario con todos los filtros
filtros={

	1:"BLUR", 
	2:"CONTOUR", 
	3:"DETAIL", 
	4:"EDGE_ENHANCE", 
	5:"EDGE_ENHANCE_MORE", 
	6:"EMBOSS", 
	7:"FIND_EDGES", 
	8:"SMOOTH", 
	9:"SMOOTH_MORE", 
	10:"SHARPEN"
}


try:

	print("¿Qué filtro desea utilizar?")
	print("BLUR -> 1\nCONTOUR -> 2\nDETAIL -> 3\nEDGE_ENHANCE -> 4\nEDGE_ENHANCE_MORE -> 5\nEMBOSS -> 6\nFIND_EDGES -> 7\nSMOOTH -> 8\nSMOOTH_MORE -> 9\nSHARPEN -> 10\n")

	choose = input()
	print(choose)

	select = filtros[int(choose)]

	print("Seleccionó -> " + select)

	##Abrimos la imagen
	img = Image.open("chester.jpg")

	if(select == "BLUR"):
		blurred(img)
	elif(select == "CONTOUR"):
		contour(img)
	elif(select == "DETAIL"):
		detail(img)
	elif(select == "EDGE_ENHANCE"):
		edge_enhance(img)
	elif(select == "EDGE_ENHANCE_MORE"):
		edge_enhance_more(img)
	elif(select == "EMBOSS"):
		emboss(img)
	elif(select == "FIND_EDGES"):
		find_edges(img)
	elif(select == "SMOOTH"):
		smooth(img)
	elif(select == "SMOOTH_MORE"):
		smoothMore(img)
	elif(select == "SHARPEN"):
		sharpen(img)

except IOError:
	print("No se encontro tu imagen >:c")
