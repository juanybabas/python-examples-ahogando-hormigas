import random

tablero = []

for x in range(0,5):
    tablero.append(["0"*5])

def print_tablero(tablero):
    for fila in tablero:
        print "".join(fila)

print "juguemos ahogar hormigas"
print_tablero(tablero)

def fila_aleatoria(tablero):
    return random.randint(0,len(tablero)-1)

def columna_aleatoria(tablero):
    return random.randint(0,len(tablero[0])-1)

hormiga_fila = fila_aleatoria(tablero)
hormiga_columna = columna_aleatoria(tablero)
print hormiga_fila
print hormiga_columna

#de aqui en adelante todo deberia ir en tu ciclo for
#asegurate de identar
adivina_fila = input("Adivina fila:")
adivina_columna = input("Adivina columna:")

if adivina_fila == hormiga_fila and adivina_columna==hormiga_columna:
    print"Felicitaciones ahogaste mi hormiga"
else:
    if(adivina_fila<0 or adivina_fila>4)or (adivina_columna<0 or adivina_columna>4):
        print"huy eso nisiquiera esta donde las hormigas"
    elif(tablero[adivina_fila][adivina_columna]=="x"):
        print"ya dijiste esa"
    else:
        print"no tocaste mi hormiga"
        tablero[adivina_fila][adivina_columna]="x"

        #mostrar turno +1 aqui
        print_tablero(tablero)


