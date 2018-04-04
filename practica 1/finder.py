from random import randint
from tkinter import *
from tkinter import ttk


class Node:
    def __init__(self, x, y, aValue):
        self.x = x
        self.y = y
        self.leftNode = 0
        self.bottomNode = 0
        self.rightNode = 0
        self.topNode = 0
        self.aValue = aValue


class AObject:
    def __init__(self, finder, start, pokemon, tablero):
        self.openQ = []
        self.closeQ = []
        self.rightWay = []
        self.steps = []

        def insertStep(node):
            if not self.rightWay:
                print('primer paso')
                self.rightWay.append(node)
                # print(self.rightWay, node, self.rightWay[0].rightNode)

            else:
                print('entre')
                for i in self.rightWay:
                    print('right', node.x, i.rightNode.x, node.y, i.rightNode.y)
                    print('left', node.x, i.leftNode.x, node.y, i.leftNode.y)
                    print('top', node.x, i.topNode.x, node.y, i.topNode.y)
                    print('bottom', node.x, i.bottomNode.x,
                          node.y, i.bottomNode.y)
                    if i.rightNode != 0:
                        if (node.x == i.rightNode.x and node.y == i.rightNode.y):
                            self.rightWay = self.rightWay[0: self.rightWay.index(
                                i) + 1]
                            break
                    if i.leftNode != 0:
                        if (node.x == i.leftNode.x and node.y == i.leftNode.y):
                            self.rightWay = self.rightWay[0: self.rightWay.index(
                                i) + 1]
                            break
                    if i.topNode != 0:
                        if (node.x == i.topNode.x and node.y == i.topNode.y):
                            self.rightWay = self.rightWay[0: self.rightWay.index(
                                i) + 1]
                            break
                    if i.bottomNode != 0:
                        if (node.x == i.bottomNode.x and node.y == i.bottomNode.y):
                            self.rightWay = self.rightWay[0: self.rightWay.index(
                                i) + 1]
                            break

        def insertClose(node):
            if self.openQ:
                for i in self.openQ:
                    if node.x == i.x and node.y == i.y:
                        self.openQ.remove(i)
                        break
            if self.closeQ:
                for i in self.closeQ:
                    if node.aValue <= i.aValue:
                        self.closeQ.insert(self.closeQ.index(i), node)
                        break
                if node.aValue > self.closeQ[-1].aValue:
                    self.closeQ.append(node)
            else:
                self.closeQ.append(node)

        def insertOpen(node):
            # print('Agregando nodo')
            if self.closeQ:
                for i in self.closeQ:
                    if node.x == i.x and node.y == i.y:
                        return
            if self.openQ:
                for i in self.openQ:
                    # print('buscando lugar para el nodo')
                    if node.aValue <= i.aValue:
                        self.openQ.insert(self.openQ.index(i), node)
                        # print('nodo agregado')
                        break
                if node.aValue > self.openQ[-1].aValue:
                    self.openQ.append(node)
                # print('nodo agregado')
            else:
                self.openQ.append(node)
                # print('primer nodo agregado')

        def findWay(goal):
            self.rightWay = []

            def wayWithoutObstacle(finder):
                obstacles = {}
                if finder.x > 0:
                    if (tablero[finder.y][finder.x - 1].name != 'Rock') and (tablero[finder.y][finder.x - 1].name != 'Van'):
                        obstacles['left'] = (True)
                    else:
                        obstacles['left'] = (False)
                else:
                    obstacles['left'] = (False)
                if finder.x < 9:
                    if (tablero[finder.y][finder.x + 1].name != 'Rock') and (tablero[finder.y][finder.x + 1].name != 'Van'):
                        obstacles['right'] = (True)
                    else:
                        obstacles['right'] = (False)
                else:
                    obstacles['right'] = (False)
                if finder.y > 0:
                    if (tablero[finder.y - 1][finder.x].name != 'Rock') and (tablero[finder.y - 1][finder.x].name != 'Van'):
                        obstacles['up'] = (True)
                    else:
                        obstacles['up'] = (False)
                else:
                    obstacles['up'] = (False)
                if finder.y < 9:
                    if (tablero[finder.y + 1][finder.x].name != 'Rock') and (tablero[finder.y + 1][finder.x].name != 'Van'):
                        obstacles['down'] = (True)
                    else:
                        obstacles['down'] = (False)
                else:
                    obstacles['down'] = (False)
                return obstacles

            def manhatan(startX, startY, goal):
                return abs(startX - goal.x) + abs(startY - goal.y)
            g_n_ = manhatan(finder.x, finder.y, start)
            h_n_ = manhatan(finder.x, finder.y, goal)
            currentTrainer = Trainer(finder.y, finder.x)
            while True:
                a = input()
                print('Pokemon', goal.x, goal.y)
                if self.openQ:
                    currentTrainer = Trainer(self.openQ[0].y, self.openQ[0].x)
                    g_n_ = manhatan(currentTrainer.x, currentTrainer.y, start)
                    h_n_ = manhatan(currentTrainer.x, currentTrainer.y, goal)

                print('Pokebola', currentTrainer.x, currentTrainer.y)
                currentNode = Node(
                    currentTrainer.x, currentTrainer.y, g_n_ + h_n_)
                obstacles = wayWithoutObstacle(currentTrainer)
                print(obstacles)
                insertClose(currentNode)
                # for k in self.closeQ:
                #     print('Cola cerrada', '[', k.x, k.y, k.aValue, ']')

                if obstacles['left']:
                    # print('izq')
                    g_n_ = manhatan(currentTrainer.x - 1,
                                    currentTrainer.y, start)
                    h_n_ = manhatan(currentTrainer.x - 1,
                                    currentTrainer.y, goal)
                    insertOpen(Node(currentTrainer.x - 1,
                                    currentTrainer.y, g_n_ + h_n_))
                    currentNode.leftNode = Node(
                        currentTrainer.x - 1, currentTrainer.y, g_n_ + h_n_)
                if obstacles['right']:
                    # print('der')
                    g_n_ = manhatan(currentTrainer.x + 1,
                                    currentTrainer.y, start)
                    h_n_ = manhatan(currentTrainer.x + 1,
                                    currentTrainer.y, goal)
                    insertOpen(Node(currentTrainer.x + 1,
                                    currentTrainer.y, g_n_ + h_n_))
                    currentNode.rightNode = Node(
                        currentTrainer.x - 1, currentTrainer.y, g_n_ + h_n_)
                if obstacles['up']:
                    # print('arriba')
                    g_n_ = manhatan(currentTrainer.x,
                                    currentTrainer.y - 1, start)
                    h_n_ = manhatan(currentTrainer.x,
                                    currentTrainer.y - 1, goal)
                    insertOpen(
                        Node(currentTrainer.x, currentTrainer.y - 1, g_n_ + h_n_))
                    currentNode.topNode = Node(
                        currentTrainer.x - 1, currentTrainer.y, g_n_ + h_n_)
                if obstacles['down']:
                    # print('abajo')
                    g_n_ = manhatan(currentTrainer.x,
                                    currentTrainer.y + 1, start)
                    h_n_ = manhatan(currentTrainer.x,
                                    currentTrainer.y + 1, goal)
                    insertOpen(
                        Node(currentTrainer.x, currentTrainer.y + 1, g_n_ + h_n_))
                    currentNode.bottomNode = Node(
                        currentTrainer.x - 1, currentTrainer.y, g_n_ + h_n_)

                insertStep(currentNode)

                # for k in self.openQ:
                #     print('Cola abierta', '[', k.x, k.y, k.aValue, ']')

                if currentTrainer.x == goal.x and currentTrainer.y == goal.y:
                    for k in self.rightWay:
                        print('Paso', '[', k.x, k.y, ']')
                    return self.rightWay

        self.steps.append(findWay(pokemon[0]))


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
    def __init__(self, i, j, container):
        self.name = 'Bean'
        self.image = PhotoImage(file='images/jelly-beans.png')
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
    def __init__(self, i, j, container=False, pokeball=False):
        self.name = 'Trainer'
        self.y = i
        self.x = j
        self.back = False
        if container:
            self.image = PhotoImage(file='images/' + pokeball + '.png')
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
        self.pokemonArray = []
        self.trainer = Trainer(randint(0, self.size), randint(
            0, self.size), self.window, 'pokeball2')

        for i in range(10):
            self.tablero.append([])
            for j in range(10):
                if ((j == self.trainer.x) & (i == self.trainer.y - 1)):
                    self.van = Van(i, j, self.window)
                    self.tablero[i].append(self.van)
                elif randint(0, 6) == 1:
                    pokemon = Pokemon(i, j, randint(1, 19), self.window)
                    self.pokemonArray.append(pokemon)
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

        def Move(trainer):
            def rightMove(leaveBean=False):
                if leaveBean:
                    # self.tablero[trainer.y][trainer.x] = Bean(trainer.y, trainer.y, self.window)
                    self.tablero[trainer.y][trainer.x + 1] = Trainer(
                        trainer.y, trainer.x + 1, self.window, 'pokeball1')
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

            def leftMove(leaveBean=False):
                if leaveBean:
                    # self.tablero[trainer.y][trainer.x] = Bean(trainer.y, trainer.y, self.window)
                    self.tablero[trainer.y][trainer.x - 1] = Trainer(
                        trainer.y, trainer.x - 1, self.window, 'pokeball1')
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

            def downMove(leaveBean=False):
                if leaveBean:
                    # self.tablero[trainer.y][trainer.x] = Bean(trainer.y, trainer.y, self.window)
                    self.tablero[trainer.y + 1][trainer.x] = Trainer(
                        trainer.y + 1, trainer.x, self.window, 'pokeball1')
                else:
                    self.tablero[trainer.y + 1][trainer.x] = Trainer(
                        trainer.y + 1, trainer.x, self.window, 'pokeball2')

                self.tablero[trainer.y][trainer.x] = Grass(
                    trainer.y, trainer.x, self.window)
                self.tablero[trainer.y][trainer.x].label.grid(
                    column=trainer.x, row=trainer.y)
                self.tablero[trainer.y +
                             1][trainer.x].label.grid(column=trainer.x, row=trainer.y + 1)
                trainer.y += 1

            def upMove(leaveBean=False):
                if leaveBean:
                    # self.tablero[trainer.y][trainer.x] = Bean(trainer.y, trainer.y, self.window)
                    self.tablero[trainer.y - 1][trainer.x] = Trainer(
                        trainer.y - 1, trainer.x, self.window, 'pokeball1')
                else:
                    self.tablero[trainer.y - 1][trainer.x] = Trainer(
                        trainer.y - 1, trainer.x, self.window, 'pokeball2')

                self.tablero[trainer.y][trainer.x] = Grass(
                    trainer.y, trainer.x, self.window)
                self.tablero[trainer.y][trainer.x].label.grid(
                    column=trainer.x, row=trainer.y)
                self.tablero[trainer.y -
                             1][trainer.x].label.grid(column=trainer.x, row=trainer.y - 1)
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

            def wayWithoutObstacle():
                obstacles = {}
                if trainer.x > 0:
                    if (self.tablero[trainer.y][trainer.x - 1].name != 'Rock') and (self.tablero[trainer.y][trainer.x - 1].name != 'Van'):
                        obstacles['left'] = (True)
                    else:
                        obstacles['left'] = (False)
                else:
                    obstacles['left'] = (False)
                if trainer.x < self.size - 1:
                    if (self.tablero[trainer.y][trainer.x + 1].name != 'Rock') and (self.tablero[trainer.y][trainer.x + 1].name != 'Van'):
                        obstacles['right'] = (True)
                    else:
                        obstacles['right'] = (False)
                else:
                    obstacles['right'] = (False)
                if trainer.y > 0:
                    if (self.tablero[trainer.y - 1][trainer.x].name != 'Rock') and (self.tablero[trainer.y - 1][trainer.x].name != 'Van'):
                        obstacles['up'] = (True)
                    else:
                        obstacles['up'] = (False)
                else:
                    obstacles['up'] = (False)
                if trainer.y < self.size - 1:
                    if (self.tablero[trainer.y + 1][trainer.x].name != 'Rock') and (self.tablero[trainer.y + 1][trainer.x].name != 'Van'):
                        obstacles['down'] = (True)
                    else:
                        obstacles['down'] = (False)
                else:
                    obstacles['down'] = (False)
                return obstacles

            def chooseWay(obstacles):
                choose = randint(0, 3)
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
                    min = abs(trainer.x + 1 - self.van.x) + \
                        abs(trainer.y - self.van.y)
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

            self.a = AObject(self.trainer, self.van,
                             self.pokemonArray, self.tablero)
            # print(self.a.openQ, self.a.closeQ)

        Move(self.trainer)
        self.window.after(500, self.findPokemon)


def main():
    tierra = Tablero(10)


# x = j | y = i
if __name__ == '__main__':
    main()
