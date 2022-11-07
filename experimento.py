lista= list()

class Libro:
    def __int__(self,titulo,genero,isbn,editorial,autor):
        self.titulo=titulo
        self.genero=genero
        self.isbn=isbn
        self.editorial=editorial
        self.autor=autor
def menu():    
    print("Menu")
    print("1.- leer")
    print("2.- listar")
    print("3.- registrar un libro nuevo")
    print("4.- borrar libro")
    print("5.- buscar por titulo o isbn")
    print("6.- ordenar por titulo")
    print("7.- buscar por autor o editorial o genero")
    print("8.- Buscar por numero de autores")
    print("9.- editar o datos de un libro")
    print("10.-Guardar")
    print("11.-salir")
    op=int(input("Escoge la opcion: "))
    if op==1:
        leer(),continuar(),menu()
    elif op==2:
        listarLibro(),continuar(),menu()
    elif op==3:
        registrarLibro(),continuar(),menu()
    elif op==4:
        borrar(),continuar(),menu()
    elif op==5:
        buscarLibro(),continuar(),menu()
    elif op==6:
        ordenar(),continuar(),menu()
    elif op==7:
        buscarAutor(),continuar(),menu()
    elif op==8:
        buscarNA(),continuar(),menu()
    elif op==9:
        editar(),continuar(),menu()
    elif op==10:
        guardar(),continuar(),menu()
    elif op==11:
        exit()
        

    else:
        menu()

def leer():
    f = open("lista_libros.txt", "r")
    leyendo = f.read()
    print(leyendo)
    f.close()

def listarLibro():
    b=0
    for a in lista:
        b+=1
        print (b,a.titulo,"",a.genero,"",a.isbn,"",a.editorial,"",a.autor)

def registrarLibro():
    a= Libro()
    a.titulo=input("ingresa el titulo: ").title()
    a.genero=input("ingresa genero: ").title()
    a.isbn=input("ingresa el isbn: ")
    a.editorial=input("ingresar la editorial: ").title()
    a.autor=input("ingresa autor: ").title()
    lista.append(a)
    
def borrar():
    listarLibro()
    borrador=int(input("Escriba el numero del libro a eliminar: "))-1
    del lista[borrador]
    print("eliminado")

    

def buscarLibro():
    print("Escogela opcion para buscar")
    print("1- Por titulo")
    print("2- Por isbn")
    p=int(input("Ingresa la opcion: "))
    if p==1:
        titulo=input("Ingresa el titulo que buscar: ").title()
        for a in lista:
            if a.titulo==titulo:
                print (a.titulo,"",a.genero,"",a.isbn,"",a.editorial,"",a.autor)
    elif p==2:
        isbn=input("Ingresa el isbn que buscar: ")
        for a in lista:
            if a.isbn==isbn:
               print (a.titulo,"",a.genero,"",a.isbn,"",a.editorial,"",a.autor)

def ordenar():
    pass

def buscarAutor():
    print("Escogela opcion para buscar")
    print("1- Por autor: ")
    print("2- Por editorial: ")
    print("3- Por genero: ")
    p=int(input("Ingresa la opcion: "))
    if p==1:
        autor=input("Ingresa el titulo que autor: ").title()
        for a in lista:
            if a.autor==autor:
                print (a.titulo,"",a.genero,"",a.isbn,"",a.editorial,"",a.autor)
    elif p==2:
        editorial=input("Ingresa el editorial que buscar: ").title()
        for a in lista:
            if a.editorial==editorial:
               print (a.titulo,"",a.genero,"",a.isbn,"",a.editorial,"",a.autor)
    elif p==3:
        genero=input("Ingresa el genero que buscar: ").title()
        for a in lista:
            if a.genero==genero:
               print (a.titulo,"",a.genero,"",a.isbn,"",a.editorial,"",a.autor)
def buscarNA():
    pass



def editar():
    pass

def guardar():
    with open('libreria.txt', 'w') as f:
        f.write(str(lista))
    print('se grabo')
    return

def continuar():
    input()
 

def salir():
    print("registro libro")



menu()
        

        