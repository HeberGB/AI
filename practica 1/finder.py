from tkinter import *
from tkinter import ttk
from random import randint

class Pokemon:
    def __init__(self, i, j, pokemonId, container):
        self.name = 'Pokemon'
        self.pokemonId = pokemonId
        self.image = PhotoImage(file='images/' + str(pokemonId) + '.png')
        self.y = i
        self.x = j
        self.label = Label(
            container,
            height='64',
            width='64',
            borderwidth='2',
            image=self.image
        )


class Grass:
    def __init__(self, i, j, container):
        self.name = 'Grass'
        self.image = PhotoImage(file='images/grass.png')
        self.y = i
        self.x = j
        self.label = Label(
            container,
            height='64',
            width='64',
            borderwidth='2',
            image=self.image
        )


class Rock:
    def __init__(self, i, j, container):
        self.name = 'Rock'
        self.image = PhotoImage(file='images/rock.png')
        self.y = i
        self.x = j
        self.label = Label(
            container,
            height='64',
            width='64',
            borderwidth='2',
            image=self.image
        )


class Trainer:
    def __init__(self, i, j, container):
        self.name = 'Trainer'
        self.image = PhotoImage(file='images/trainer.png')
        self.y = i
        self.x = j
        self.label = Label(
            container,
            height='64',
            width='64',
            borderwidth='2',
            image=self.image
        )


class Van:
    def __init__(self, i, j, container):
        self.name = 'Van'
        self.image = PhotoImage(file='images/van.png')
        self.y = i
        self.x = j
        self.label = Label(
            container,
            height='64',
            width='64',
            borderwidth='2',
            image=self.image
        )


class Tablero:
    def __init__(self, length):
        self.window = Tk()
        self.window.title('Pokemon Finder')
        self.size = IntVar()
        self.tablero = []

        builded = False
        self.x = -1
        self.y = -1
        self.x2 = -1
        self.y2 = -1
        for i in range(10):
            self.tablero.append([])
            for j in range(10):
                if randint(0, 50) == 3 & builded == False:
                    self.x = j
                    self.y = i+1
                    builded = True
                    van = Van(i, j, self.window)
                    self.tablero[i].append(van)
                elif (j == self.x) & (i == self.y):
                    trainer = Trainer(i, j, self.window)
                    self.tablero[i].append(trainer)
                elif randint(0, 6) == 1:
                    pokemon = Pokemon(i, j, randint(1, 19), self.window)
                    self.tablero[i].append(pokemon)
                elif randint(0, 6) == 1:
                    rock = Rock(i, j, self.window)
                    self.tablero[i].append(rock)
                else:
                    grass = Grass(i, j, self.window)
                    self.tablero[i].append(grass)

        for i in range(10):
            for j in range(10):
                self.tablero[i][j].label.grid(
                    column=self.tablero[i][j].x, row=self.tablero[i][j].y)

        self.window.after(500, self.findPokemon)
        self.window.mainloop()

    def findPokemon(self):
        def Move():
            def rightMove():
                self.tablero[self.y][self.x + 1] = Trainer(self.y, self.x + 1, self.window)
                self.tablero[self.y][self.x] = Grass(self.y, self.x, self.window)
                self.tablero[self.y][self.x].label.grid(column=self.x, row=self.y)
                self.tablero[self.y][self.x + 1].label.grid(column=self.x + 1, row=self.y)
                self.x += 1

            def leftMove():
                self.tablero[self.y][self.x - 1] = Trainer(self.y, self.x - 1, self.window)
                self.tablero[self.y][self.x] = Grass(self.y, self.x, self.window)
                self.tablero[self.y][self.x].label.grid(column=self.x, row=self.y)
                self.tablero[self.y][self.x - 1].label.grid(column=self.x - 1, row=self.y)
                self.x -= 1

            def downMove():
                self.tablero[self.y + 1][self.x] = Trainer(self.y + 1, self.x, self.window)
                self.tablero[self.y][self.x] = Grass(self.y, self.x, self.window)
                self.tablero[self.y][self.x].label.grid(column=self.x, row=self.y)
                self.tablero[self.y + 1][self.x].label.grid(column=self.x, row=self.y + 1)
                self.y += 1

            def upMove():
                self.tablero[self.y - 1][self.x] = Trainer(self.y, self.x, self.window)
                self.tablero[self.y][self.x] = Grass(self.y, self.x, self.window)
                self.tablero[self.y][self.x].label.grid(column=self.x, row=self.y)
                self.tablero[self.y - 1][self.x].label.grid(column=self.x, row=self.y - 1)
                self.y -= 1

            def isPokemonClose():
                if self.x < 9 and self.tablero[self.y][self.x+1].name == 'Pokemon':
                    return 'right'
                elif self.x > 0 and self.tablero[self.y][self.x-1].name == 'Pokemon':
                    return 'left'
                elif self.y < 9 and self.tablero[self.y + 1][self.x].name == 'Pokemon':
                    return 'down'
                elif self.y > 0 and self.tablero[self.y - 1][self.x].name == 'Pokemon':
                    return 'up'
            
            def wayWithoutObstacle():
                obstacles = {}
                if self.x > 0:
                    if (self.tablero[self.y][self.x - 1].name != 'Rock') and (self.tablero[self.y][self.x - 1].name != 'Van'):
                        obstacles['left']=(True)
                    else:
                        obstacles['left']=(False)
                else:
                    obstacles['left']=(False)
                if self.x < 9:
                    if (self.tablero[self.y][self.x + 1].name != 'Rock') and (self.tablero[self.y][self.x + 1].name != 'Van'):
                        obstacles['right']=(True)
                    else:
                        obstacles['right']=(False)
                else:
                    obstacles['right']=(False)
                if self.y > 0:
                    if (self.tablero[self.y - 1][self.x].name != 'Rock') and (self.tablero[self.y - 1][self.x].name != 'Van'):
                        obstacles['up']=(True)
                    else:
                        obstacles['up']=(False)
                else:
                    obstacles['up']=(False)
                if self.y < 9:
                    if (self.tablero[self.y + 1][self.x].name != 'Rock') and (self.tablero[self.y + 1][self.x].name != 'Van'):
                        obstacles['down']=(True)
                    else:
                        obstacles['down']=(False)
                else:
                    obstacles['down']=(False)
                return obstacles

            def chooseWay(obstacles):
                choose = randint(0,3)
                if choose == 0 and obstacles['left']:
                    return 'left'
                elif choose == 1 and obstacles['right']:
                    return 'right'
                elif choose == 2 and obstacles['up']:
                    return 'up'
                elif choose == 3 and obstacles['down']:
                    return 'down'
                else:
                    return chooseWay(obstacles)
            
            def backToVan():
                print('regreso a van')
            
            try:
                if isPokemonClose() == 'right':
                    rightMove()
                    backToVan()
                elif isPokemonClose() == 'left':
                    leftMove()
                    backToVan()
                elif isPokemonClose() == 'down':
                    downMove()
                    backToVan()
                elif isPokemonClose() == 'up':
                    upMove()               
                    backToVan()
                else:
                    way = chooseWay(wayWithoutObstacle())
                    if way == 'left':
                        leftMove()
                    elif way == 'right':
                        rightMove()
                    elif way == 'up':
                        upMove()
                    elif way == 'down':
                        downMove()
            except Exception as error:
                print(error)
        Move()
        self.window.after(500, self.findPokemon)


def main():
    tierra = Tablero('Pokemon Finder')


# x = j | y = i
if __name__ == '__main__':
    main()
