
#defino los atributos de libro
class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.ISBN = ISBN
        self.editorial = editorial
        self.autores = autores

class Menu:
    def __init__(self):
        self.agregar_libro =[]
        
    #menu opciones
    def opciones(self):
        print()
    
        opciones_list = [
                 ['1. Leer archivo'],
                 ['2. Listar libro'],
                 ['3. Agregar libro'],
                 ['4. Eliminar libro'],
                 ['5. Buscar Libro ISBN o Título'],
                 ['6. Ordenar libro'],
                 ['7. Buscar libro por autor o editorial o genero'],
                 ['8. Buscar por número de autores'],
                 ['9. Actualizar datos-libro título-género-ISBN-editorial-autor'],
                 ['10. Guardar libro'],
                 ['11. Salir']
        ]

        #rango de opciones
        for i in range(11):
            print(opciones_list[i][0])
        
        opcion = int(input("Ingrese una opción del 1 al 11:  "))

        if opcion == 1:
            return leer()

        elif opcion == 2:
           return listar()

        elif opcion == 3:
            return agregar(),listar()
            

        elif opcion == 4:
            return borrar(),listar()

        elif opcion == 5:
            return buscar()

        elif opcion == 6:
            return 

        elif opcion == 7:
            return 

        elif opcion == 8:
            return 

        elif opcion == 9:
            return 

        elif opcion == 10:
            return 

        elif opcion == 11:
            print("Usted ha salido del menu")
            exit()

        self.opciones()

# dict data 
lista_titulos = {"1" : "nada" , "2": "dinero", "3" : "Cartero"}
datos = {'ID1' : {
                        'Título' : 'Cartero',
                        'Autor'  : 'Charles Bukowski',
                        'Género' : 'Drama',
                        'ISBN'   : '9788433920638',
                        'Editorial' : 'Black Sparrow Books'

                    },

             'ID2' :  {   'Título' : 'Dinero',
                        'Autor'  : 'Martin Amis',
                        'Género' : 'Ficción',
                        'ISBN'   : '9788433920492',
                        'Editorial' : 'Anagrama'

                    },

              'ID3' : {   'Título' : 'Nada',
                        'Autor'  : 'Carmen Laforet',
                        'Género' : 'Novela',
                        'ISBN'   : '9788423342792',
                        'Editorial' : 'Austral'

              }}   



# opcion 1 resultados
def leer():
    f = open("lista_libros.txt", "r")
    leyendo = f.read()
    print(leyendo)
    f.close()
    return


# opcion 2 resultados
def listar():

    for l in datos:
        print("\n",l)
        for d in datos[l]:
            print('{}:{}'.format(d,datos[l][d]))
      
    return
   
def agregar():
    nuevo_id = input("Ingrese el ID: ")
    nuevo_titulo = input("Ingrese el nombre del libro: ").title()
    nuevo_genero = input("Ingrese el genero: ").title()
    nuevo_ISBN = input("Ingrese ISBN: ")
    nuevo_editorial = input("Ingrese la editorial: ").title()
    nuevo_autor = input("Ingrese el autor: ").title()
    
    a={nuevo_id:{'Título':nuevo_titulo,'Autor':nuevo_autor,'Género':nuevo_genero,'ISBN':nuevo_ISBN, 'Editorial':nuevo_editorial}}
    datos.update(a)
    
    
    
    return

def borrar():
    eliminar = str(input("Ingrese el ID a eliminar: "))
    datos.pop(eliminar)
    return

def buscar():
    #titulo nuero
    #i=0
    #while i<3:
    #    busqueda=str(input("Escribe lo que buscar por Titulo o ISBN: "))
    #    for x in datos.items():
    #        if x in datos[i]["Título"]:
    #            break
    pass    


bliblioteca = Menu()
bliblioteca.opciones()