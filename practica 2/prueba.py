from random import randint
from tkinter import *
from tkinter import ttk


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


class Bean:
    def __init__(self, i, j, container, img):
        self.name = 'Bean'
        self.them = False
        self.image = PhotoImage(file='images/' + img + '.png')
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
    def __init__(self, i, j, container, pokeball):
        self.name = 'Trainer'
        self.image = PhotoImage(file='images/' + pokeball + '.png')
        self.y = i
        self.x = j
        self.back = False
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
    def __init__(self, size):
        self.window = Tk()
        self.window.title('Pokemon Finder')
        self.size = size
        self.tablero = []
        self.trainer = Trainer(randint(0, self.size), randint(
            0, self.size), self.window, 'pokeball2')
        # self.trainer2 = Trainer(randint(0, self.size), randint(
            # 0, self.size), self.window, 'pokeball2')
        pokemonos = [0, 0]
        for i in range(10):
            self.tablero.append([])
            for j in range(10):
                if ((j == self.trainer.x) & (i == self.trainer.y - 1)):
                    self.van = Van(i, j, self.window)
                    self.tablero[i].append(self.van)
                elif pokemonos[0] < 3 and pokemonos[0] > 0:
                    pokemon = Pokemon(i, j, randint(1, 19), self.window)
                    self.tablero[i].append(pokemon)
                    pokemonos[0] += 1
                elif pokemonos[1] < 3 and pokemonos[1] > 0:
                    pokemon = Pokemon(i, j, randint(1, 19), self.window)
                    self.tablero[i].append(pokemon)
                    pokemonos[1] += 1
                elif randint(0, 6) == 1:
                    pokemon = Pokemon(i, j, randint(1, 19), self.window)
                    self.tablero[i].append(pokemon)
                    pokemonos[0] += 1
                    pokemonos[1] += 1
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
        def Move(trainer):
            def rightMove(leaveBean=False, takeIt=False):
                if leaveBean:
                    self.tablero[trainer.y][trainer.x + 1] = Trainer(
                        trainer.y, trainer.x + 1, self.window, 'pokeball1')
                    if takeIt:
                        bean = Bean(trainer.y, trainer.x,
                                    self.window, 'jelly-bean')
                        bean.them = True
                        self.tablero[trainer.y][trainer.x] = bean
                    else:
                        self.tablero[trainer.y][trainer.x] = Bean(
                            trainer.y, trainer.x, self.window, 'jelly-beans')

                else:
                    self.tablero[trainer.y][trainer.x + 1] = Trainer(
                        trainer.y, trainer.x + 1, self.window, 'pokeball2')
                    self.tablero[trainer.y][trainer.x] = Grass(
                        trainer.y, trainer.x, self.window)

                self.tablero[trainer.y][trainer.x].label.grid(
                    column=trainer.x, row=trainer.y)
                self.tablero[trainer.y][trainer.x +
                    1].label.grid(column=trainer.x + 1, row=trainer.y)
                trainer.x += 1

            def leftMove(leaveBean=False, takeIt=False):
                if leaveBean:
                    self.tablero[trainer.y][trainer.x - 1] = Trainer(
                        trainer.y, trainer.x - 1, self.window, 'pokeball1')
                    if takeIt:
                        bean = Bean(trainer.y, trainer.x,
                                    self.window, 'jelly-bean')
                        bean.them = True
                        self.tablero[trainer.y][trainer.x] = bean
                    else:
                        self.tablero[trainer.y][trainer.x] = Bean(
                            trainer.y, trainer.x, self.window, 'jelly-beans')

                else:
                    self.tablero[trainer.y][trainer.x - 1] = Trainer(
                        trainer.y, trainer.x - 1, self.window, 'pokeball2')
                    self.tablero[trainer.y][trainer.x] = Grass(
                        trainer.y, trainer.x, self.window)

                self.tablero[trainer.y][trainer.x].label.grid(
                    column=trainer.x, row=trainer.y)
                self.tablero[trainer.y][trainer.x -
                    1].label.grid(column=trainer.x - 1, row=trainer.y)
                trainer.x -= 1

            def downMove(leaveBean=False, takeIt=False):
                if leaveBean:
                    self.tablero[trainer.y + 1][trainer.x] = Trainer(
                        trainer.y + 1, trainer.x, self.window, 'pokeball1')
                    if takeIt:
                        bean = Bean(trainer.y, trainer.x,
                                    self.window, 'jelly-bean')
                        bean.them = True
                        self.tablero[trainer.y][trainer.x] = bean
                    else:
                        self.tablero[trainer.y][trainer.x] = Bean(
                            trainer.y, trainer.x, self.window, 'jelly-beans')
                else:
                    self.tablero[trainer.y + 1][trainer.x] = Trainer(trainer.y + 1, trainer.x, self.window, 'pokeball2')                    
                    self.tablero[trainer.y][trainer.x] = Grass(trainer.y, trainer.x, self.window)
                    
                self.tablero[trainer.y][trainer.x].label.grid(column=trainer.x, row=trainer.y)
                self.tablero[trainer.y + 1][trainer.x].label.grid(column=trainer.x, row=trainer.y + 1)
                trainer.y += 1

            def upMove(leaveBean=False, takeIt=False):
                if leaveBean:
                    self.tablero[trainer.y - 1][trainer.x] = Trainer(trainer.y - 1, trainer.x, self.window, 'pokeball1')
                    if takeIt:
                        bean = Bean(trainer.y, trainer.x, self.window, 'jelly-bean')
                        bean.them = True
                        self.tablero[trainer.y][trainer.x] = bean
                    else:
                        self.tablero[trainer.y][trainer.x] = Bean(trainer.y, trainer.x, self.window, 'jelly-beans')
                else:
                    self.tablero[trainer.y - 1][trainer.x] = Trainer(trainer.y - 1, trainer.x, self.window, 'pokeball2')                    
                    self.tablero[trainer.y][trainer.x] = Grass(trainer.y, trainer.x, self.window)
                
                self.tablero[trainer.y][trainer.x].label.grid(column=trainer.x, row=trainer.y)
                self.tablero[trainer.y - 1][trainer.x].label.grid(column=trainer.x, row=trainer.y - 1)
                trainer.y -= 1

            def isPokemonClose():
                if trainer.x < self.size - 1 and self.tablero[trainer.y][trainer.x+1].name == 'Pokemon':
                    return 'right'
                elif trainer.x > 0 and self.tablero[trainer.y][trainer.x-1].name == 'Pokemon':
                    return 'left'
                elif trainer.y < self.size - 1 and self.tablero[trainer.y + 1][trainer.x].name == 'Pokemon':
                    return 'down'
                elif trainer.y > 0 and self.tablero[trainer.y - 1][trainer.x].name == 'Pokemon':
                    return 'up'

            def isBeanClose():
                if trainer.x < self.size - 1 and self.tablero[trainer.y][trainer.x+1].name == 'Bean' and self.tablero[trainer.y][trainer.x+1].them:
                    return 'right'
                elif trainer.x > 0 and self.tablero[trainer.y][trainer.x-1].name == 'Bean' and self.tablero[trainer.y][trainer.x-1].them:
                    return 'left'
                elif trainer.y < self.size - 1 and self.tablero[trainer.y + 1][trainer.x].name == 'Bean' and self.tablero[trainer.y+1][trainer.x].them:
                    return 'down'
                elif trainer.y > 0 and self.tablero[trainer.y - 1][trainer.x].name == 'Bean' and self.tablero[trainer.y-1][trainer.x].them:
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
                if trainer.x < self.size - 1:
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
                if trainer.y < self.size - 1:
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

                def chooseBackWay():
                    min = abs(trainer.x + 1 - self.van.x) + abs(trainer.y - self.van.y)
                    if (abs(trainer.x - 1 - self.van.x) + abs(trainer.y - self.van.y) < min) and wayWithoutObstacle()['left'] and isPokemonClose() != 'left':
                        return 'left'
                    elif (abs(trainer.x - self.van.x) + abs(trainer.y + 1 - self.van.y) < min) and wayWithoutObstacle()['down'] and isPokemonClose() != 'down':
                        return 'down'
                    elif (abs(trainer.x - self.van.x) + abs(trainer.y - 1 - self.van.y) < min) and wayWithoutObstacle()['up'] and isPokemonClose() != 'up':
                        return 'up'
                    elif wayWithoutObstacle()['right'] and isPokemonClose() != 'right':
                        return 'right'
                    else:
                        None
                
                def isVanClose():
                    if self.trainer.x < self.size - 1:
                        if self.tablero[trainer.y][trainer.x+1].name == 'Van':
                            return True
                    if self.trainer.x > 0:
                        if self.tablero[trainer.y][trainer.x-1].name == 'Van':
                            return True
                    if self.trainer.y < self.size - 1:
                        if self.tablero[trainer.y+1][trainer.x].name == 'Van':
                            return True
                    if self.trainer.y > 0:
                        if self.tablero[trainer.y-1][trainer.x].name == 'Van':
                            return True
                    else:
                        return False
                
                pokemonGotcha(True)
                
                try:
                    if isVanClose():
                        pokemonGotcha(False)
                    elif chooseBackWay() == 'right':
                        rightMove(True)
                    elif chooseBackWay() == 'left':
                        leftMove(True)
                    elif chooseBackWay() == 'down':
                        downMove(True)
                    elif chooseBackWay() == 'up':
                        upMove(True)
                
                except Exception as error:
                    print(error)
                    
            def pokemonGotcha(gotIt):
                self.trainer.back = gotIt
                self.trainer.image = PhotoImage(file='images/pokeball1.png')
                self.trainer.label.config(image=self.trainer.image)
            
            try:
                if trainer.back == True:
                    backToVan()
                elif isPokemonClose() == 'right':
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
                elif isBeanClose() == 'right':
                    rightMove(True, True)
                elif isBeanClose() == 'left':
                    leftMove(True, True)
                elif isBeanClose() == 'down':
                    downMove(True, True)
                elif isBeanClose() == 'up':
                    upMove(True, True)
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
                print(trainer.back)
            except Exception as error:
                print(error)
        Move(self.trainer)
        # Move(self.trainer2)
        self.window.after(500, self.findPokemon)


def main():
    tierra = Tablero(10)


# x = j | y = i
if __name__ == '__main__':
    main()
