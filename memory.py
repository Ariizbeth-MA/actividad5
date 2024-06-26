"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
cont_taps= 0 # Se inicializa el contador de los taps en 0
cont_matches = 0  # Se inicializa el contador de las parejas en 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global cont_taps
    cont_taps +=1 #Empieza a contar los taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        global cont_matches
        cont_matches +=1 # Empiez a contar las parejas 


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()

        # x en 26.8 y y en y+1 para que quede centrado
        goto(x + 26.8, y + 1)
        #Se cambia el color del cuadrado dependiendo del tile que se muestre
        color(tiles[mark]*5, 255 - tiles[mark]*4, 255 - tiles[mark]*4)
        write(tiles[mark],align = "center", font=('Arial', 30, 'normal'))

    goto (0,210) # Contador que se mostrara
    write (cont_taps, font =("Arial", 15))
    if cont_matches == 32:
       up()
       goto(0,0)
       color('purple')
       write ("Ganaste", align = "center", font= ("Arial",15,"bold")) # Contador de parejas encontradas y mensaje de que el jugador ha ganado  

    update()

    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
colormode(255) #Modificaciones en RGB
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
