


from Tkinter import *
from math import *
from numpy import *
from tkMessageBox import *

class UnionFind:
        #This is the classic Union find class that we went over in class
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
                #below line generates the coordinates for the initial start of the dot
                self.coordinates = [[20, 20, 20, o_w], [20, o_w, o_w-20, o_w], [o_w, o_w, o_w, \
                                        20], [o_w, 20, 40, 20]]

                self.generate_maze(dimension)
        
        def generate_maze(self, dimension):
                self.walls = []
                self.wall_check = []
                checker = 0
                skip_line = 1
                tally = 1
                #this section of code runs through a for loop to create a list of "walls" in my program
                #(0, 1), (0, 5), (1, 2) etc.
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
                #this section of code takes a random number and grabs a wall from my list
                #self.current_walls above is the list that this section of code will cycle through in order
                #to make sure that each of the sections are either connected compoments or have a wall deleted
                        self.current_walls.remove(self.current_walls[num])
                        if not UF.connected(i, j):
                                UF.union(i, j)
                                self.wall_check = self.wall_check + [[i, j]]
                        else:
                                tally = 0
                                orig_i = i
                                orig_j = j
                #if the section is already connected and I want to draw an line in Tkinter I figure out
                #what section of the theoretical grid that wall should be in by reducing it to its
                #lowest value 0 through N (dimensions of maze). That's what the below section does 
                                while i >= dimension or j >= dimension:
                                        if i >= dimension:
                                                i = i-dimension
                                        if j >= dimension:
                                                j = j-dimension
                                        tally += 1
                                if orig_j-orig_i != 1:
                #this section adds coordinates of the walls based on the position of the wall that was
                #found in the above code
                #i and j are those reduced values and tally just keep track of how many times it was reduced
                #which nicely turns out to be the position of the wall on the y axis
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
        #pretty straightforward section. I draw the lines here based on the coordinates list
        #the i<4 section is just to make the outside lines a different color
                        if i < 4:
                                self.window.create_line(list_points[i][0], list_points[i][1], \
                                        list_points[i][2], list_points[i][3], fill="red")
                        else:
                                self.window.create_line(list_points[i][0], list_points[i][1], \
                                        list_points[i][2], list_points[i][3], fill="blue")      



        def draw_ball(self, shift_y, shift_x):
                self.total_y = self.total_y + shift_y
                self.total_x = self.total_x + shift_x
                ty = self.total_y
                tx = self.total_x

                #I use these values to keep track of where the dot should be
                        #these make the move_ball function easy to implement, by just changing the x or y
                        #coordinates by a certain value, essentially a translation

                self.coordinates = self.coordinates + \
                        [[28+tx, 28+ty, 28+tx, 32+ty], [29+tx, 28+ty, 29+tx, 32+ty], \
                        [30+tx, 28+ty, 30+tx, 32+ty], [31+tx, 28+ty, 31+tx, 32+ty], \
                        [32+tx, 28+ty, 32+tx, 32+ty]]

                self.draw_maze(self.coordinates)


        def move_ball(self, event):
                #locale value coordinates the location of the dot with the list of walls so
                #that the dot doesn't go through walls it shouldn't
                #in these functions is also the code that erases the dot if the dot retraces its steps
                #this code also allows for a cheat where you leave the maze through the top of the initial
                #position, that coding is the self.counter part of the puzzle. self.counter will always be
                #0, unless you press i (and move up) from position 0,0. If you move up from 0,0, you will
                #be able to move the dot freely around the map. If you move the dot in a specific way you
                #can still win! but you will have cheated. (this specific implementation only works for a
                #20x20 size map)
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



                        





if __name__ == "__main__":
        # create a Tkinter 
        window = Canvas(Tk(), width=700, height=700)
        window.pack()

        # create a 2D object
        n = 30
        UF = UnionFind(n)
        my_maze = Maze(n, window)
        #can also have sys.argv or raw_input() to allow the user to choose the file
        #box.txt is simply the file that I created for this program to use, any
        #other similarly ordered text file would also work, such as rectangle

        # define function that captures keyboard events
        window.bind_all("<Key>", my_maze.move_ball)

        # start the event handler
        mainloop()



















