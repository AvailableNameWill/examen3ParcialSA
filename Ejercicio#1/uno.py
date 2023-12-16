import json
import sys
from datetime import datetime

clubs_array = []
honors_arr = []


def valid_date(date_str):
    try:
        datetime.strptime(date_str, '%b %d, %Y')
        return True
    except ValueError:
        return False


with open('player_data.json', 'r') as file:
    data = json.load(file)

print('Jugadores \n')

name = input('Ingrese el nombre del jugador: \n')
if len(name) > 2:
    data["name"] = name
else:
    print('Nombre muy corto')
    sys.exit()
pos = input('Ingrese la posicion del jugador: \n')
if len(pos) > 2:
    data["position"] = pos
else:
    print('valores incorrectos, al menos escriba la abreviatura de la posicion')
    sys.exit()
nat = input('Ingrese la nacionalidad del jugador: \n')
if len(nat) > 2:
    data["nationality"] = nat
else:
    print('valores incorrectos, al menos escriba la abreviatura de la nacionalidad')
    sys.exit()
while True:
    date = input('Ingrese la fecha de nacimiento del jugador, ejm: Jun 25, 1986 \n')
    if valid_date(date):
        data["date_of_birth"] = date
        break
    else:
        print('Se le especifico el formato especifico')


num = int(input('En cuantos clubes jugo? \n'))

if num <= 0:
    print('No es posible!!')
    sys.exit()
if num == 1:
    club = input('Ingrese el nombre del equipo: \n')
    period = input('Ingrese el periodo en que estuvo el jugador: \n')
    nclub = {"name": club, "period": period}
    clubs_array.append(nclub)
    data["clubs"] = clubs_array
if num > 1:
    for _ in range(num):
        club = input('Ingrese el nombre del equipo: \n')
        period = input('Ingrese el periodo en que estuvo el jugador: \n')
        nclub = {"name": club, "period": period}
        clubs_array.append(nclub)
    data["clubs"] = clubs_array

print('Ingrese los titulos mas importantes que gano el jugador, si no ha ganado escriba "nada" ')

for _ in range(5):
    hon = input('Ingrese el nombre del titulo: \n')
    honors_arr.append(hon)
data["honors"] = honors_arr

with open('player_data.json', 'w') as file:
    json.dump(data, file, indent=2)

print('data saved')
