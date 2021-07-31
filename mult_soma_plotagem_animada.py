# animated_line_plot.py
from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def soma_algarismo(dado_recebido):
    def soma_alga(dado):
        lista_numeros = list(map(lambda trans_num: int(trans_num),
                                 filter(lambda retira_num: retira_num.isnumeric(), str(dado))))
        return sum(lista_numeros)

    final = soma_alga(dado_recebido)
    while final >= 10:
        final = soma_alga(str(final))
    return final


# create empty lists for the x and y data
x = []
y = []

# create the figure and axes objects
fig, ax = plt.subplots()


# function that draws each frame of the animation
def animate(i):

    pt = [soma_algarismo(5 * num) for num in range(1, 10)][i]
    x.append(i)
    y.append(pt)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

    print(i)
    print(pt)
    print(f'{x} {y}')
    print()


# run the animation
ani = FuncAnimation(fig, animate, frames=9, interval=500, repeat=False)

ani.save('main7.gif', writer='imagemagick')
