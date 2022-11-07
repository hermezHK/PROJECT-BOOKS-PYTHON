import requests

url_api = "https://pokeapi.co/api/v2/pokemon/"
#habilidad links
habilidad1  ="https://pokeapi.co/api/v2/ability/1/"
habilidad2  ="https://pokeapi.co/api/v2/ability/2/"
habilidad3  ="https://pokeapi.co/api/v2/ability/3/"
habilidad4  ="https://pokeapi.co/api/v2/ability/4/"
# forma links
poke_forma1  = "https://pokeapi.co/api/v2/pokemon-shape/1/"
poke_forma2  = "https://pokeapi.co/api/v2/pokemon-shape/2/"
poke_forma3  = "https://pokeapi.co/api/v2/pokemon-shape/3/"
poke_forma4  = "https://pokeapi.co/api/v2/pokemon-shape/4/"
poke_forma_url = "https://pokeapi.co/api/v2/pokemon-shape/"

#l generacion links
generacion1 = "https://pokeapi.co/api/v2/generation/1/"
generacion2 = "https://pokeapi.co/api/v2/generation/2/"
generacion3 = "https://pokeapi.co/api/v2/generation/3/"
generacion4 = "https://pokeapi.co/api/v2/generation/4/"


# parámetro para mostrar el nombre del menú
def mostrar_menu(nombre, opciones): 
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ').lower()) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

#  parámetro para salir  del menú
def generar_menu(nombre, opciones, opcion_salida):  
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        

# se  genera menú principal
def menu_principal():
    opciones = {
        '1': ('Lista de pokemon por generacion.', submenu1),
        '2': ('Lista de pokemon según su forma', submenu2),  
        '3': ('Lista de habilidad pokemon', submenu3),
        '4': ('Salir', salir)
    }
    # indicamos regreso al menu
    generar_menu('Menú principal', opciones, '4')  

# definimos el submenu
def submenu1():
    opciones = {
        'a': ('Generacion1', funcionA),
        'b': ('Generacion2', funcionB),
        'c': ('Generacion3', funcionC),
        'd': ('Generacion4', funcionD),
        'e': ('Volver al menú principal', salir)
    }

    # indicamos regreso al menu
    generar_menu('Submenú', opciones, 'e')


def submenu2():
    opciones = {
        'a': ('ball', funcionForm1),
        'b': ('squiggle', funcionForm2),
        'c': ('fish', funcionForm3),
        'd': ('ball', funcionForm4),
        'e': ('Volver al menú principal', salir)
    }

    # indicamos regreso al menu
    generar_menu('Submenú', opciones, 'e')    



def submenu3():
    opciones = {
        'a': ('stench', funcionHabilidad1),
        'b': ('drizzle', funcionHabilidad2),
        'c': ('speed-boost', funcionHabilidad3),
        'd': ('battle-armor', funcionHabilidad4),
        'e': ('Volver al menú principal', salir)
    }

    # indicamos regreso al menu
    generar_menu('Submenú', opciones, 'e')  
     




# sub menu respuesta opcion ---------------------------------(a)#

def funcionA():
    response = requests.get( generacion1 )
    data  = response.json()
    img_url  = [pokeimg['url'] for pokeimg in data['pokemon_species']]
    list_poke_generacion = [generacion['name'] for generacion in data['pokemon_species']]
    lista_habilidades = [habilidad['name'] for habilidad in data['moves']]
    print("generacion 1 :\n ",list_poke_generacion)
    for i in zip(list_poke_generacion, lista_habilidades, img_url):
        print(i)
    
   

def funcionB():
    response = requests.get( generacion2 )
    data  = response.json()
    img_url  = [pokeimg['url'] for pokeimg in data['pokemon_species']]
    list_poke_generacion = [generacion['name'] for generacion in data['pokemon_species']]
    lista_habilidades = [habilidad['name'] for habilidad in data['moves']]
    for i in zip(list_poke_generacion, lista_habilidades, img_url):
        print(i)



def funcionC():
    response = requests.get( generacion3 )
    data  = response.json()
    img_url  = [pokeimg['url'] for pokeimg in data['pokemon_species']]
    list_poke_generacion = [generacion['name'] for generacion in data['pokemon_species']]
    lista_habilidades = [habilidad['name'] for habilidad in data['moves']]
    for i in zip(list_poke_generacion, lista_habilidades, img_url):
        print(i)



def funcionD():
    response = requests.get( generacion4 )
    data  = response.json()
    img_url  = [pokeimg['url'] for pokeimg in data['pokemon_species']]
    list_poke_generacion = [generacion['name'] for generacion in data['pokemon_species']]
    lista_habilidades = [habilidad['name'] for habilidad in data['moves']]
    for i in zip(list_poke_generacion, lista_habilidades, img_url):
        print(i)


#--------------------------------------------------------------------------------------------#
#opcin 2 respuestas sub menu 

def funcionForm1():
    

    response = requests.get( poke_forma1 )
    data  = response.json()
    list_poke_forma = [forma['name'] for forma in data['pokemon_species']]
    list_forma_url = [forma['url'] for forma in data['pokemon_species']]
    for i in zip(list_poke_forma, list_forma_url):
        print(i)
    




def funcionForm2():
    
    response = requests.get( poke_forma2 )
    data  = response.json()
    list_poke_forma = [forma['name'] for forma in data['pokemon_species']]
    list_forma_url = [forma['url'] for forma in data['pokemon_species']]
    for i in zip(list_poke_forma, list_forma_url):
        print(i)




def funcionForm3():
    

    response = requests.get( poke_forma3 )
    data  = response.json()
    list_poke_forma = [forma['name'] for forma in data['pokemon_species']]
    list_forma_url = [forma['url'] for forma in data['pokemon_species']]
    for i in zip(list_poke_forma, list_forma_url):
        print(i)




def funcionForm4():
    

    response = requests.get( poke_forma4 )
    data  = response.json()
    list_poke_forma = [forma['name'] for forma in data['pokemon_species']]
    list_forma_url = [forma['url'] for forma in data['pokemon_species']]
    for i in zip(list_poke_forma, list_forma_url):
        print(i)


#-----------------------------------------------------------------------------------------------------------#


def funcionHabilidad1():
    response = requests.get( habilidad1 )
    data  = response.json()
    list_poke_habilidad = [habilidades['pokemon']['name'] for habilidades in data['pokemon']]
    poke_habilidad_link = [habilidades['pokemon']['url'] for habilidades in data['pokemon']]
    for i in zip(list_poke_habilidad, poke_habilidad_link):
        print(i)





def funcionHabilidad2():
    response = requests.get( habilidad2 )
    data  = response.json()
    list_poke_habilidad = [habilidades['pokemon']['name'] for habilidades in data['pokemon']]
    poke_habilidad_link = [habilidades['pokemon']['url'] for habilidades in data['pokemon']]
    for i in zip(list_poke_habilidad, poke_habilidad_link):
        print(i)





def funcionHabilidad3():
    response = requests.get( habilidad3 )
    data  = response.json()
    list_poke_habilidad = [habilidades['pokemon']['name'] for habilidades in data['pokemon']]
    poke_habilidad_link = [habilidades['pokemon']['url'] for habilidades in data['pokemon']]
    for i in zip(list_poke_habilidad, poke_habilidad_link):
        print(i)




def funcionHabilidad4():
    response = requests.get( habilidad4 )
    data  = response.json()
    list_poke_habilidad = [habilidades['pokemon']['name'] for habilidades in data['pokemon']]
    poke_habilidad_link = [habilidades['pokemon']['url'] for habilidades in data['pokemon']]
    for i in zip(list_poke_habilidad, poke_habilidad_link):
        print(i)






# def funcionHabilidad1():
# def funcionHabilidad1():




def salir():
    print('Saliendo')

# inicializando

if __name__ == '__main__':
    menu_principal()














