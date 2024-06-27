Generos=["Horror","ficcion","ciencia"]
lista_libros=[]

def RegistrarLibro():   
    Titulo=input("ingrese Titulo del Libro: ").lower
    while Titulo==" ":
        print("intente nuevamente")
        Titulo=input("ingrese Titulo del Libro: ").lower

    Autor=input("ingrese Autor del Libro: ").lower
        
    Genero=input("ingrese el tipo de genero del libro: ").lower
        
    precio=int(input("ingrese el Valor del libro: "))

    #almacenar en un diccionario
    lista_libros.append({"Titulo": Titulo,
                "autor": Autor,
                "Genero": Genero,
                "Precio": precio,
    })
    

def ListarTodosLosLibros():
    for i in range(len(lista_libros)):


def RegistrarVenta(lista_libros):
    TituloV=input("ingrese nombre del Libro: ").lower
    if TituloV not in lista_libros:
        print("Libro no existe, pruebe nuevamente")
        TituloV=input("ingrese nombre del Libro: ").lower
    Cantidad=int(input("ingrese la cantidad "))

def imprimirReporteVentas(lista_libros):
    

def GenerarTxt():
    GeneroSeleccionado=("ingrese genero de libro a imprimir o presione enter para imprimir todos")
    if GeneroSeleccionado=="":
        Genero_a_imprimir==lista_libros
        nombreArchivo="TodosLosLibros.txt"
    elif GeneroSeleccionado in Generos:
        Genero_a_imprimir=[]

        #def GenerarTxt(): intento2
            #with open ({Generos})

#Me falto tiempo para resolverlo  :(