import requests

url_pokeapi="https://pokeapi.co/api/v2/generation/"

def getPokemon():
    buscador=str(input("Ingrese el numero de la generacion: "))
    response = requests.get(url_pokeapi + buscador)
    data=response.json()
    pokeSpecies=[]
    for nombre in data['pokemon_species']:
        pokeSpecies.append(nombre['name'])

    
    for x in pokeSpecies:
        print(x)


    
    #print(f"Nombre: {data(['pokemon_species'])}")
    #print(f"Nombre: {data['url']}")



def menu():    
    print("Menu")
    print("1.- listar pokemon por generacion")
    print("2.- pokemon por forma")
    print("3.- listar por habilidad")
    print("4.- listar habitat")
    print("5.- listar por tipo")
    
    print("11.-salir")
    op=int(input("Escoge la opcion: "))
    if op==1:
        getPokemon(),continuar(),menu()
    elif op==2:
        continuar(),menu()
    elif op==3:
        continuar(),menu()
    elif op==4:
        continuar(),menu()
    elif op==5:
        continuar(),menu()
    elif op==6:
          exit()

def continuar():
    input()
    return

menu()



