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
    def Move(self, way):
        if way == 'right':
            self.x += 1
            # self.label.grid(column=self.x, row=self.y)
            
        elif way == 'left':
            self.x -= 1
            # self.label.grid(column=self.x, row=self.y)

        elif way == 'down':
            self.y += 1
            # self.label.grid(column=self.x, row=self.y)

        elif way == 'up':
            self.y += 1
            # self.label.grid(column=self.x, row=self.y)
        
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
    def __init__(self, size):
        self.window = Tk()
        self.window.title('Pokemon Finder')
        self.size = size
        self.tablero = []
        self.pokemon = []
        self.van = None
        self.trainer = None

        #Filling grass matrix (list of lists) and show them in GUI
        for i in range(self.size):
            self.tablero.append([])
            for j in range(self.size):

                if randint(0, 20) == 6 and self.van == None:
                    self.van = Van(i, j, self.window)
                    self.van.label.grid(column = self.van.x, row = self.van.y)
                    self.tablero[i].append(Grass(i, j, self.window))

                elif self.van != None and self.trainer == None and (j == self.van.x) and (i == self.van.y + 1):
                    self.trainer = Trainer(i, j, self.window)
                    self.tablero[i].append(Grass(i, j, self.window))
                    self.trainer.label.grid(column = self.trainer.x, row = self.trainer.y)

                #Filling pokemon list with random property position
                elif randint(0, 6) == 1:
                    self.tablero[i].append(Pokemon(i, j, randint(1, 19), self.window))
                    #Seting pokemon to a GUI cell                  
                    self.tablero[i][j].label.grid(column = j, row = i)
                    
                elif randint(0, 6) == 1:
                    self.tablero[i].append(Rock(i, j, self.window))
                    #Seting to a GUI cell
                    self.tablero[i][j].label.grid(column = j, row = i)

                else:
                    self.tablero[i].append(Grass(i, j, self.window))
                    #Seting to a GUI cell
                    self.tablero[i][j].label.grid(column = j, row = i)
        self.window.after(500, self.findPokemon)
        self.window.mainloop()

    def update(self):
        for i in range(self.size):
            for j in range(self.size):
                self.tablero[i][j].label.grid(column = j, row = i)
    
    def pokemonTaken(self, pokemon):
        self.tablero[pokemon.y][pokemon.x] = (Grass(pokemon.y, pokemon.x, self.window))

    def findPokemon(self):
        def Move(trainer):
            def rightMove():
                self.update()
                trainer.Move('right')
                trainer.label.grid(column=trainer.x, row=trainer.y)
                

            def leftMove():
                self.update()
                trainer.Move('left')
                trainer.label.grid(column=trainer.x, row=trainer.y)

            def downMove():
                self.update()
                trainer.Move('down')
                trainer.label.grid(column=trainer.x, row=trainer.y)

            def upMove():
                self.update()
                trainer.Move('up')
                trainer.label.grid(column=trainer.x, row=trainer.y)

            def isPokemonClose():
                if trainer.x < self.size and self.tablero[trainer.y][trainer.x+1].name == 'Pokemon':
                    return 'right'
                elif trainer.x > 0 and self.tablero[trainer.y][trainer.x-1].name == 'Pokemon':
                    return 'left'
                elif trainer.y < self.size and self.tablero[trainer.y + 1][trainer.x].name == 'Pokemon':
                    return 'down'
                elif trainer.y > 0 and self.tablero[trainer.y - 1][trainer.x].name == 'Pokemon':
                    return 'up'
            
            def wayWithoutObstacle():
                obstacles = {}
                if trainer.x > 0:
                    if (self.tablero[trainer.y][trainer.x - 1].name != 'Rock') and (self.tablero[trainer.y][trainer.x - 1].name != 'Van'):
                        obstacles['left']=(True)
                    else:
                        obstacles['left']=(False)
                else:
                    obstacles['left']=(False)
                if trainer.x < 9:
                    if (self.tablero[trainer.y][trainer.x + 1].name != 'Rock') and (self.tablero[trainer.y][trainer.x + 1].name != 'Van'):
                        obstacles['right']=(True)
                    else:
                        obstacles['right']=(False)
                else:
                    obstacles['right']=(False)
                if trainer.y > 0:
                    if (self.tablero[trainer.y - 1][trainer.x].name != 'Rock') and (self.tablero[trainer.y - 1][trainer.x].name != 'Van'):
                        obstacles['up']=(True)
                    else:
                        obstacles['up']=(False)
                else:
                    obstacles['up']=(False)
                if trainer.y < 9:
                    if (self.tablero[trainer.y + 1][trainer.x].name != 'Rock') and (self.tablero[trainer.y + 1][trainer.x].name != 'Van'):
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
                print(trainer.x, trainer.y)
                if isPokemonClose() == 'right':
                    self.pokemonTaken(self.tablero[trainer.y][trainer.x + 1])
                    rightMove()
                    backToVan()
                elif isPokemonClose() == 'left':
                    self.pokemonTaken(self.tablero[trainer.y][trainer.x - 1])
                    leftMove()
                    backToVan()
                elif isPokemonClose() == 'down':
                    self.pokemonTaken(self.tablero[trainer.y + 1][trainer.x])
                    downMove()
                    backToVan()
                elif isPokemonClose() == 'up':
                    self.pokemonTaken(self.tablero[trainer.y - 1][trainer.x])
                    upMove()               
                    backToVan()
                else:
                    print('in')
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
        Move(self.trainer)
        self.window.after(500, self.findPokemon)


def main():
    tierra = Tablero(10)


# x = j | y = i
if __name__ == '__main__':
    main()
