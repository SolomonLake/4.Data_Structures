


from Tkinter import *
from math import *
from numpy import *
from tkMessageBox import *

class UnionFind:
        def __init__(self, dimension):
                dimension = int(dimension)
                self.N = dimension*dimension
                self.nodes = [0] * self.N
                self.sz = [1] * self.N

                for i in range(0, self.N):
                        self.nodes[i] = i

        def find(self, i):
                while i != self.nodes[i]:
                        self.nodes[i] = self.nodes[self.nodes[i]]
                        i = self.nodes[i]
                return i


        def connected(self, p, q):
                return self.find(p) == self.find(q)

        def union(self, p, q):
                i = self.find(p)
                j = self.find(q)
                if self.sz[i] < self.sz[j]:
                        self.nodes[i] = j
                        self.sz[j] += self.sz[i]
                else:
                        self.nodes[j] = i
                        self.sz[i] += self.sz[i]


class Maze:
        def __init__(self, dimension, win):
                dimension = int(dimension)
                self.window = win
                self.total_y = 0
                self.total_x = 0
                self.walls = []
                self.current_walls = []
                self.locale = [0, 0]
                self.locale_list = [0, 0]
                self.counter = 0
                self.dimension = dimension
                o_w = dimension*20+20
                #outer wall
                self.coordinates = [[20, 20, 20, o_w], [20, o_w, o_w-20, o_w], [o_w, o_w, o_w, \
                                        20], [o_w, 20, 40, 20]]

                self.generate_maze(dimension)
        
        def generate_maze(self, dimension):
                self.walls = []
                self.wall_check = []
                checker = 0
                skip_line = 1
                tally = 1
                for i in range(0, dimension*dimension):
                        if checker == i:
                                value = tally*dimension-1
                                checker = value
                                if skip_line == 1:
                                        skip_line = 0
                                else:
                                        skip_line = 1
                                tally += 1
                        if skip_line == 0:
                                self.walls.append([i, i+1])
                        if i < (dimension*dimension-dimension):
                                self.walls.append([i, i+dimension])
                        skip_line = 0
                self.current_walls = self.walls
                
                random.seed()
                while len(self.current_walls) != 0:
                        num = random.randint(0, len(self.current_walls))
                        i = self.current_walls[num][0]
                        j = self.current_walls[num][1]
                        self.current_walls.remove(self.current_walls[num])
                        if not UF.connected(i, j):
                                UF.union(i, j)
                                self.wall_check = self.wall_check + [[i, j]]
                        else:
                                tally = 0
                                orig_i = i
                                orig_j = j
                                while i >= dimension or j >= dimension:
                                        if i >= dimension:
                                                i = i-dimension
                                        if j >= dimension:
                                                j = j-dimension
                                        tally += 1
                                if orig_j-orig_i != 1:
                                        self.coordinates = self.coordinates + [[20+i*20,\
                                                20+tally*20, 20+(i+1)*20, 20+tally*20]]
                                else:
                                        self.coordinates = self.coordinates + [[20+j*20, \
                                                20+tally*20, 20+j*20, 20+(tally+1)*20]]
                self.coordinates = self.coordinates + [[28, 28, 28, 32], [29, 28, 29, 32], \
                        [30, 28, 30, 32], [31, 28, 31, 32], [32, 28, 32, 32]]
                self.draw_ball(0, 0)


        def draw_maze(self, list_points):
                self.window.delete("all")
                for i in range (0, len(list_points)-1):
                        if i < 4:
                                self.window.create_line(list_points[i][0], list_points[i][1], \
                                        list_points[i][2], list_points[i][3], fill="red")
                        else:
                                self.window.create_line(list_points[i][0], list_points[i][1], \
                                        list_points[i][2], list_points[i][3], fill="blue")      

#       def draw_ball(self, shift_y, shift_x):
#               self.total_y = self.total_y + shift_y
#               self.total_x = self.total_x + shift_x
#               self.coordinates_ball = [[28, 28, 28, 32], [29, 28, 29, 32], \
#                       [30, 28, 30, 32], [31, 28, 31, 32], [32, 28, 32, 32]]
#               for i in range (0, 3):
#                       self.window.create_line(self.coordinates_ball[i][0], \
#               self.coordinates_ball[i][1], self.coordinates_ball[i][2], \
#               self.coordinates_ball[i][3], fill="red")
#
#               self.locale = [0, 0]


        def draw_ball(self, shift_y, shift_x):
                self.total_y = self.total_y + shift_y
                self.total_x = self.total_x + shift_x
                ty = self.total_y
                tx = self.total_x
#               if self.counter == 1:   
#                       for i in range (0, 3):
#                               self.coordinates.remove(self.coordinates[len(self.coordinates)-1])
#               if self.counter == 0:
#                       for i in range (0, 5):
#                               self.coordinates.remove(self.coordinates[len(self.coordinates)-1])
#               for i in range (0, 5):
#                       self.coordinates.remove(self.coordinates[len(self.coordinates)-1])
                self.coordinates = self.coordinates + \
                        [[28+tx, 28+ty, 28+tx, 32+ty], [29+tx, 28+ty, 29+tx, 32+ty], \
                        [30+tx, 28+ty, 30+tx, 32+ty], [31+tx, 28+ty, 31+tx, 32+ty], \
                        [32+tx, 28+ty, 32+tx, 32+ty]]

                self.draw_maze(self.coordinates)


        def move_ball(self, event):
                if event.char == 'l':
                        self.locale[1] = self.locale[1] + 1
                        if self.counter == 0:
                                if self.locale in self.wall_check:
                                        self.locale[0] = self.locale[0] + 1
                                        locale = [[self.locale[0], self.locale[1]]]
                                        locale_check = [self.locale[0], self.locale[1]]
                                        if locale_check not in self.locale_list:
                                                self.locale_list = self.locale_list + locale
                                        else:
                                                for i in range (0, 10):
                                                        self.coordinates.remove(self.coordinates[len(self.coordinates)-1])
                                                self.locale_list.remove(self.locale_list[len(self.locale_list)-1])
                                        self.draw_ball(0, 20)
                                else:
                                        self.locale[1] = self.locale[1] - 1
                        else:
                                self.draw_ball(0, 20)
                        if self.locale == [self.dimension**2-1, self.dimension**2-1]:
                                showinfo('Ok', 'You Win!! Well done!')

#                               else:
#                                       for i in range (0, 3):
#                                               self.coordinates.remove(self.coordinates[len(self.coordinates)-1])



                if event.char == 'k':
                        self.locale[1] = self.locale[1] + self.dimension
                        if self.counter == 0:
                                if self.locale in self.wall_check:
                                        self.locale[0] = self.locale[0] + self.dimension
                                        locale = [[self.locale[0], self.locale[1]]]
                                        locale_check = [self.locale[0], self.locale[1]]
                                        if locale_check not in self.locale_list:
                                                self.locale_list = self.locale_list + locale
                                        else:
                                                for i in range (0, 10):
                                                        self.coordinates.remove(self.coordinates[len(self.coordinates)-1])
                                                self.locale_list.remove(self.locale_list[len(self.locale_list)-1])
                                        self.draw_ball(20, 0)
                                else:
                                        self.locale[1] = self.locale[1] - self.dimension
                        else:
                                self.draw_ball(20, 0)
                        if self.locale == [self.dimension**2-1, self.dimension**2-1]:
                                showinfo('Ok', 'You Win!! Well done!')

#                               else:
#                                       for i in range (0, 3):
#                                               self.coordinates.remove(self.coordinates[len(self.coordinates)-1])



                if event.char == 'i':
                        if self.locale[0] == 0 and self.locale[1] == 0:
                                self.counter = 1
                        self.locale[0] = self.locale[0] - self.dimension
                        if self.counter == 0:
                                if self.locale in self.wall_check:
                                        self.locale[1] = self.locale[1] - self.dimension
                                        locale = [[self.locale[0], self.locale[1]]]
                                        locale_check = [self.locale[0], self.locale[1]]
                                        if locale_check not in self.locale_list:
                                                self.locale_list = self.locale_list + locale
                                        else:
                                                for i in range (0, 10):
                                                        self.coordinates.remove(self.coordinates[len(self.coordinates)-1])
                                                self.locale_list.remove(self.locale_list[len(self.locale_list)-1])

                                        self.draw_ball(-20, 0)
                                else:
                                        self.locale[0] = self.locale[0] + self.dimension
                        else:
                                self.draw_ball(-20, 0)
                        if self.locale == [-41, 440]:
                                showinfo('Ok', 'You Win!! But you cheated... Naughty naughty.')
#                               else:
#                                       for i in range (0, 3):
#                                               self.coordinates.remove(self.coordinates[len(self.coordinates)-1])



                if event.char == 'j':
                        self.locale[0] = self.locale[0] - 1
                        if self.counter == 0:
                                if self.locale in self.wall_check:
                                        self.locale[1] = self.locale[1] - 1
                                        locale = [[self.locale[0], self.locale[1]]]
                                        locale_check = [self.locale[0], self.locale[1]]
                                        if locale_check not in self.locale_list:
                                                self.locale_list = self.locale_list + locale
                                        else:
                                                for i in range (0, 10):
                                                        self.coordinates.remove(self.coordinates[len(self.coordinates)-1])
                                                self.locale_list.remove(self.locale_list[len(self.locale_list)-1])
                                        self.draw_ball(0, -20)
                                else:
                                        self.locale[0] = self.locale[0] + 1
                        else:
                                self.draw_ball(0, -20)
#                               else:
#                                       for i in range (0, 3):
#                                               self.coordinates.remove(self.coordinates[len(self.coordinates)-1])



                        





if __name__ == "__main__":
        # create a Tkinter 
        window = Canvas(Tk(), width=700, height=700)
        window.pack()

        # create a 2D object
        n = raw_input('Enter dimensions here: ')
        UF = UnionFind(n)
        my_maze = Maze(n, window)
        #can also have sys.argv or raw_input() to allow the user to choose the file
        #box.txt is simply the file that I created for this program to use, any
        #other similarly ordered text file would also work, such as rectangle

        # define function that captures keyboard events
        window.bind_all("<Key>", my_maze.move_ball)

        # start the event handler
        mainloop()



















