

from Tkinter import *
from math import *

class Object2D:
	def __init__(self, currentfile, win):

		self.wndw = win

		#get lines
		lines = [line.strip() for line in open(currentfile)]

		num_points = int(lines[0])

		self.my2dobj = []

		for i in range(num_points):
			self.my2dobj.append(map(int,lines[i+1].split()))
			

		
		self.draw_object()

	def key_pressed(self, event):
		if event.char == 'i':
			self.translate(0, -5)
		elif event.char == 'j':
			self.translate(-5, 0)
		elif event.char == 'k':
			self.translate(0, 5)
		elif event.char == 'l':
			self.translate(5, 0)
		elif event.char == 'w':
			self.scale(.5)
		elif event.char == 's':
			self.scale(-.5)
		elif event.char == 'a':
			self.rotate(-5)
		elif event.char == 'd':
			self.rotate(5)
		self.draw_object()

	def translate(self, dx, dy):
		for seg in self.my2dobj:
			seg[0] += dx
			seg[1] += dy
			seg[2] += dx
			seg[3] += dy

	def scale(self, s):
		average_x = 0
		average_y = 0
		for seg in self.my2dobj:
			average_x += seg[0]
			average_x += seg[2]
			average_y += seg[1]
			average_y += seg[3]
		average_x = average_x/((len(self.my2dobj))*2)
		average_y = average_y/((len(self.my2dobj))*2)
		#this entire above section is just finding the averages of x and y
		self.translate(-average_x, -average_y)
		for seg in self.my2dobj:
			seg[0] += seg[0] * s
			seg[1] += seg[1] * s
			seg[2] += seg[2] * s
			seg[3] += seg[3] * s
		self.translate(average_x, average_y)

	def rotate(self, degree):
		average_x = 0
		average_y = 0
		for seg in self.my2dobj:
			average_x += seg[0]
			average_x += seg[2]
			average_y += seg[1]
			average_y += seg[3]
		average_x = average_x/((len(self.my2dobj))*2)
		average_y = average_y/((len(self.my2dobj))*2)
		self.translate(-average_x, -average_y)
		cosine_radians = radians(degree)
		cur_cosine = cos(cosine_radians)
		sine_radians = radians(degree)
		cur_sine = sin(sine_radians)
		for seg in self.my2dobj:
			seg[0] = seg[0] * cur_cosine - seg[1] * cur_sine
			seg[1] = seg[0] * cur_sine + seg[1] * cur_cosine
			seg[2] = seg[2] * cur_cosine - seg[3] * cur_sine
			seg[3] = seg[2] * cur_sine + seg[3] * cur_cosine
		self.translate(average_x, average_y)


	def draw_object(self):
		self.wndw.delete("all")
		for seg in self.my2dobj:
			self.wndw.create_line(seg[0], seg[1], seg[2], seg[3], fill="blue")
			print seg


class Point2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def translate(self, dx, dy):
		x += dx
		y += dy



class Line2D:
	def __init__(self, coordinates):
		self.x1 = coordinates[0]
		self.y1 = coordinates[1]
		self.x2 = coordinates[2]
		self.y2 = coordinates[3]


	def scale(self, s):
		average_x = 0
		average_y = 0
		for seg in self.my2dobj:
			average_x += seg[0]
			average_x += seg[2]
			average_y += seg[1]
			average_y += seg[3]
		average_x = average_x/((len(self.my2dobj))*2)
		average_y = average_y/((len(self.my2dobj))*2)
		self.translate(-average_x, -average_y)
		for seg in self.my2dobj:
			seg[0] += seg[0] * s
			seg[1] += seg[1] * s
			seg[2] += seg[2] * s
			seg[3] += seg[3] * s
		self.translate(average_x, average_y)

		
		


if __name__ == "__main__":
	# create a Tkinter 
	window = Canvas(Tk(), width=500, height=500)
	window.pack()

	# create a 2D object
	obj2d = Object2D('face.txt', window)
	#can also have sys.argv or raw_input() to allow the user to choose the file
	#box.txt is simply the file that I created for this program to use, any
	#other similarly ordered text file would also work, such as rectangle

	# define function that captures keyboard events
	window.bind_all("<Key>", obj2d.key_pressed)

	# start the event handler
	mainloop()


