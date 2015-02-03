# BST GUI by Eric
# Updated Apr 23 11:51 PM

# YOU MUST PUT YOUR BST CLASS FILE "BST.PY" IN THE SAME FOLDER WITH THIS FILE
from BST import *

from Tkinter import *
import copy

class GUI():
        def __init__(self, myBST):
                # IF YOU WANT TO SHOW MORE NODES PROPERLY, DECREASE THE FONT SIZE
                self.font_size = 12
                
                self.BST = myBST
                self.window = Tk()
                self.window.title("A Binary Search Tree GUI by Eric")
                self.bg, self.fg = "gray", "gray97"
                self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
                self.window.geometry(str(self.w) + "x" + str(self.h))
                self.window.bind_all("<Key>", self.key_pressed)
                self.canvas = Canvas(self.window, bg=self.bg, highlightbackground=self.bg, width=self.w, height=self.h)
                self.canvas.place(x=0, y=0)
                self.rsize, self.csize = self.font_size*2, self.font_size*2
                self.draw()
                self.undoKey, self.undoValue = None, None
                
                pos = self.w*0.5-65
                Label(self.window, text="Key: ", bg=self.bg, font=("Lucida Grande", self.font_size+1)).place(x=pos-170, y=self.h*0.8-64, anchor=E)
                Label(self.window, text="Value (Insert only): ", bg=self.bg, font=("Lucida Grande", self.font_size+1)).place(x=pos-170, y=self.h*0.8-32, anchor=E)
                self.returnLabel = Label(self.window, text="Method returns: ", bg=self.bg, font=("Lucida Grande", self.font_size+1))
                self.returnLabel.place(x=pos-170, y=self.h*0.8, anchor=E)
                
                self.keyEntry = Entry(self.window, bg=self.fg, highlightbackground=self.bg, width=8)
                self.keyEntry.place(x=pos-170, y=self.h*0.8-64, anchor=W)
                self.valueEntry = Entry(self.window, bg=self.fg, highlightbackground=self.bg, width=8)
                self.valueEntry.place(x=pos-170, y=self.h*0.8-32, anchor=W)
                self.returnEntry = Entry(self.window, bg=self.fg, highlightbackground=self.bg, width=8)
                self.returnEntry.place(x=pos-170, y=self.h*0.8, anchor=W)
                
                Button(self.window, text="Insert", width=8, highlightbackground=self.bg, command=self.insert).place(x=pos, y=self.h*0.8-64, anchor=CENTER)
                delButton = Button(self.window, text="Delete", width=8, highlightbackground=self.bg, command=self.delete)
                delButton.place(x=pos, y=self.h*0.8-32, anchor=CENTER)
                self.undoButton = Button(self.window, text="Undo", width=8, state=DISABLED, highlightbackground=self.bg, command=self.undo)
                self.undoButton.place(x=pos, y=self.h*0.8, anchor=CENTER)
                searchButton = Button(self.window, text="Search", width=8, highlightbackground=self.bg, command=self.search)
                searchButton.place(x=pos+130, y=self.h*0.8-64, anchor=CENTER)
                floorButton = Button(self.window, text="Floor", width=8, highlightbackground=self.bg, command=self.floor)
                floorButton.place(x=pos+130, y=self.h*0.8-32, anchor=CENTER)
                ceilingButton = Button(self.window, text="Ceiling", width=8, highlightbackground=self.bg, command=self.ceiling)
                ceilingButton.place(x=pos+130, y=self.h*0.8, anchor=CENTER)
                sizeButton = Button(self.window, text="Size", width=8, highlightbackground=self.bg, command=self.size)
                sizeButton.place(x=pos+260, y=self.h*0.8-64, anchor=CENTER)
                rankButton = Button(self.window, text="Rank", width=8, highlightbackground=self.bg, command=self.rank)
                rankButton.place(x=pos+260, y=self.h*0.8-32, anchor=CENTER)
                self.selectionButton = Button(self.window, text="Selection", width=8, highlightbackground=self.bg, command=self.rank)
                self.selectionButton.place(x=pos+260, y=self.h*0.8, anchor=CENTER)
                
                menubar = Menu(self.window)
                fileMenu = Menu(menubar)
                searchMenu = Menu(menubar)
                countMenu = Menu(menubar)
                showMenu = Menu(menubar)
                menubar.add_cascade(label="File", menu=fileMenu)
                menubar.add_cascade(label="Search", menu=searchMenu)
                menubar.add_cascade(label="Count", menu=countMenu)
                menubar.add_cascade(label="Show", menu=showMenu)
                self.window.config(menu=menubar)
                fileMenu.add_command(label="Insert", command=self.insert)
                if hasattr(BST, "delete"):
                        fileMenu.add_command(label="Delete", command=self.delete)
                else:
                        fileMenu.add_command(label="Delete", command=self.delete, state=DISABLED)
                        delButton.config(state=DISABLED)
                fileMenu.add_command(label="Quit", command=self.quit)
                if hasattr(BST, "search") or hasattr(BST, "range"):
                        searchMenu.add_command(label="Key / Range", command=self.search)
                else:
                        searchMenu.add_command(label="Key / Range", command=self.search, state=DISABLED)
                        searchButton.config(state=DISABLED)
                if hasattr(BST, "floor"):
                        searchMenu.add_command(label="Floor", command=self.floor)
                else:
                        searchMenu.add_command(label="Floor", command=self.floor, state=DISABLED)
                        floorButton.config(state=DISABLED)
                if hasattr(BST, "ceiling"):
                        searchMenu.add_command(label="Ceiling", command=self.ceiling)
                else:
                        searchMenu.add_command(label="Ceiling", command=self.ceiling, state=DISABLED)
                        ceilingButton.config(state=DISABLED)
                if hasattr(BST, "size"):
                        countMenu.add_command(label="Size", command=self.size)
                else:
                        countMenu.add_command(label="Size", command=self.size, state=DISABLED)
                        sizeButton.config(state=DISABLED)
                if hasattr(BST, "rank"):
                        countMenu.add_command(label="Rank", command=self.rank)
                else:
                        countMenu.add_command(label="Rank", command=self.rank, state=DISABLED)
                        rankButton.config(state=DISABLED)
                if hasattr(BST, "selection"):
                        countMenu.add_command(label="Selection", command=self.selection)
                else:   
                        countMenu.add_command(label="Selection", command=self.selection, state=DISABLED)
                        self.selectionButton.config(state=DISABLED)
                if hasattr(BST, "minimum"):
                        showMenu.add_command(label="Minimum", command=self.minimum)
                else:
                        showMenu.add_command(label="Minimum", command=self.minimum, state=DISABLED)
                if hasattr(BST, "maximum"):
                        showMenu.add_command(label="Maximum", command=self.maximum)
                else:
                        showMenu.add_command(label="Maximum", command=self.maximum, state=DISABLED)
                
        def draw(self, cx=None, cy=None, space=None, node=None, from_here_on=None, blueX=[None], blueRange=(None, None)):
                if space is None:
                        cx = self.w*0.5
                        cy = self.rsize
                        space = self.w*0.25
                        node = self.BST.root
                        self.canvas.delete(ALL)
                        self.canvas.create_line(0, self.h-310, self.w, self.h-310)
                
                if node:
                        highlight = False
                        if node.key == from_here_on:
                                from_here_on = True
                                highlight = True
                        elif node in blueX or node.key in blueX:
                                highlight = True
                        else:
                                blueList = list(blueRange)
                                if (blueList[0] is None) and (blueList[1] is not None):
                                        blueList[0] = node.key - 1
                                if (blueList[1] is None) and (blueList[0] is not None):
                                        blueList[1] = node.key + 1
                                if node.key > blueList[0] and node.key < blueList[1]:
                                        highlight = True
                        
                        if (highlight == True) or (from_here_on == True):
                                self.canvas.create_rectangle(cx-self.csize*1.5, cy, cx+self.csize*1.5, cy+self.rsize, fill="deep sky blue")
                                self.canvas.create_rectangle(cx-self.csize*1.5, cy+self.rsize, cx+self.csize*1.5, cy+self.rsize*2, fill="deep sky blue")
                        else:
                                self.canvas.create_rectangle(cx-self.csize*1.5, cy, cx+self.csize*1.5, cy+self.rsize, fill=self.fg)
                                self.canvas.create_rectangle(cx-self.csize*1.5, cy+self.rsize, cx+self.csize*1.5, cy+self.rsize*2, fill=self.fg)

                        self.canvas.create_line(cx-self.csize*0.5, cy, cx-self.csize*0.5, cy+self.rsize*2)
                        self.canvas.create_line(cx+self.csize*0.5, cy, cx+self.csize*0.5, cy+self.rsize*2)
                        
                        self.canvas.create_text(cx-self.csize, cy+self.rsize*0.5, anchor=CENTER, text="K")
                        self.canvas.create_text(cx, cy+self.rsize*0.5, anchor=CENTER, text="V")
                        self.canvas.create_text(cx+self.csize, cy+self.rsize*0.5, anchor=CENTER, text="N")
                        
                        self.canvas.create_text(cx, cy+self.rsize*1.5, anchor=CENTER, text=str(node.value)[:2])
                        self.canvas.create_text(cx-self.csize, cy+self.rsize*1.5, anchor=CENTER, text=str(node.key))
                        if hasattr(node, "N"):
                                self.canvas.create_text(cx+self.csize, cy+self.rsize*1.5, anchor=CENTER, text=str(node.N))
                        
                        if node.left:
                                self.canvas.create_line(cx-self.csize*1.5, cy+self.rsize, cx-space+self.csize*1.5, cy+self.rsize*4)
                                self.draw(cx-space, cy+self.rsize*3, space*0.5, node.left, from_here_on=from_here_on, blueX=blueX, blueRange=blueRange)
                        if node.right:
                                self.canvas.create_line(cx+self.csize*1.5, cy+self.rsize, cx+space-self.csize*1.5, cy+self.rsize*4)
                                self.draw(cx+space, cy+self.rsize*3, space*0.5, node.right, from_here_on=from_here_on, blueX=blueX, blueRange=blueRange)

        def get_key(self):
                if self.keyEntry.get():
                        key = self.keyEntry.get()
                        while " " in key:
                                key = key.replace(" ", "")
                        try:
                                if "." in key:
                                        key = float(key)
                                else:
                                        key = int(key)
                                return key
                        except ValueError:
                                return self.keyEntry.get()
        
        def process_returned(self, returned):
                blueX = []
                if isinstance(returned, Node):
                        blueX.append(returned)
                        return blueX, True
                elif type(returned) == float or type(returned) == int:
                        blueX.append(returned)
                        return blueX, False
                elif type(returned) == tuple or type(returned) == list:
                        for x in returned:
                                if isinstance(x, Node):
                                        blueX.append(x)
                        if len(blueX) > 0:
                                return blueX, True
                        for x in returned:
                                if type(x) == float or type(x) == int:
                                        blueX.append(x)
                        return blueX, False
                else:
                        return blueX, None
        
        def update_return(self, returned, fn):
                self.returnEntry.delete(0, END)
                self.returnEntry.insert(0, str(returned))
                self.returnLabel.config(text=fn)
                return
                                
        def insert(self, k=None, v=None, multiple=False):
                if k is None:
                        k = self.get_key()
                if type(k) == float or type(k) == int:
                        if v is None:
                                v = self.valueEntry.get()
                        if multiple is False:
                                self.undoKey = k
                                self.undoValue = v
                                self.undoButton.config(text="Undo", state=NORMAL)
                                self.undoAction = 'BST.insert(' + str(k) + ', "' + v + '")'
                                self.lastBST = copy.deepcopy(self.BST)
                        returned = self.BST.insert(k, v)
                        self.update_return(returned, 'BST.insert(' + str(k) + ', "' + v + '") returns: ')
                        if multiple is False:
                                self.draw(blueX=[k])
                                self.canvas.create_text(self.w*0.5, self.h-345, anchor=S, text='I updated the tree according to your "insert" method and highlighted the node with key ' + str(k) + ' for you.')
                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Tip: You can insert multiple keys by entering more than one number, e.g. "1, 2, 3, 4."')
                elif type(k) == str:
                        if "," in k:
                                while " " in k:
                                        k = k.replace(" ", "")
                                k = k.split(",")
                                for i in xrange(len(k)):
                                        try:
                                                if "." in k[i]:
                                                        k[i] = float(k[i])
                                                else:
                                                        k[i] = int(k[i])
                                        except ValueError:
                                                k[i] = None
                                while None in k:
                                        k.remove(None)
                                self.undoKey = k
                                if v is None:
                                        v = self.valueEntry.get()
                                        self.undoValue = v
                                self.undoButton.config(text="Undo", state=NORMAL)
                                self.undoAction = 'Inserting multiple keys.'
                                self.insert(k, v)
                
                elif type(k) == list:
                        self.lastBST = copy.deepcopy(self.BST)
                        for i in xrange(len(k)):
                                self.insert(k[i], v, multiple = True)
                        self.draw(blueX=k)
                        t = str(k).replace("[", "").replace("]", "")
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='I updated the tree according to your "insert" method and highlighted the node with keys ' + t + ' for you.')
                        
        def delete(self, k=None, multiple = False):
                if k is None:
                        k = self.get_key()
                if type(k) == float or type(k) == int:
                        self.undoValue = None
                        if multiple is False:
                                self.undoKey = k
                                self.undoButton.config(text="Undo", state=NORMAL)
                                self.undoAction = "BST.delete(" + str(k) + ")"
                                self.lastBST = copy.deepcopy(self.BST)
                                key_exists = True
                                if hasattr(BST, "search"):
                                        if self.BST.search(k) is None:
                                                key_exists = False
                        returned = self.BST.delete(k)
                        self.update_return(returned, "BST.delete(" + str(k) + ") returns: ")
                        if multiple is False:
                                self.draw()
                                if key_exists is False:
                                        self.canvas.create_text(self.w*0.5, self.h-345, anchor=S, text="The key " + str(k) + " does not exist in your tree. The tree should be the same as before.")
                                else:
                                        self.canvas.create_text(self.w*0.5, self.h-345, anchor=S, text='I updated the tree according to your "delete" method.')
                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Tip: You can delete multiple keys by entering more than one number, e.g. "1, 2, 3, 4."')
                                
                elif type(k) == str:
                        if "," in k:
                                while " " in k:
                                        k = k.replace(" ", "")
                                k = k.split(",")
                                for i in xrange(len(k)):
                                        try:
                                                if "." in k[i]:
                                                        k[i] = float(k[i])
                                                else:
                                                        k[i] = int(k[i])
                                        except ValueError:
                                                k[i] = None
                                while None in k:
                                        k.remove(None)
                                self.undoKey = k
                                self.undoValue = None
                                self.undoButton.config(text="Undo", state=NORMAL)
                                self.undoAction = 'Removing multiple keys.'
                                self.delete(k, multiple = True)
                
                elif type(k) == list:
                        self.lastBST = copy.deepcopy(self.BST)
                        for i in xrange(len(k)):
                                self.delete(k[i], multiple = True)
                        self.draw()
                        t = str(k).replace("[", "").replace("]", "")
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='I updated the tree according to your "delete" method.')
        
        def undo(self):
                self.returnEntry.delete(0, END)
                self.returnLabel.config(text="Method returns: ")
                if self.undoButton["text"] == "Undo":
                        self.BST = self.lastBST
                        self.draw()
                        self.undoButton.config(text="Redo")
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text="The following action has been undone: " + self.undoAction)
                else:
                        self.undoButton.config(text="Undo")
                        if self.undoValue is not None:
                                self.insert(self.undoKey, self.undoValue)
                        else:
                                self.delete(self.undoKey)
                        
        def search(self):
                # range
                k = self.keyEntry.get()
                if k.count(",") == 1:
                        while " " in k:
                                k = k.replace(" ", "")
                        k = k.split(",")
                        try:
                                for i in xrange(len(k)):
                                        if "." in k[i]:
                                                k[i] = float(k[i])
                                        else:
                                                k[i] = int(k[i])
                                if hasattr(BST, "range"):
                                        returned = self.BST.range(k[0], k[1])
                                        self.update_return(returned, "BST.range(" + str(k[0]) + ", " + str(k[1]) + ") returns: ")
                                        x = self.process_returned(returned)
                                        if x[1] is not None:
                                                self.draw(blueX = x[0])
                                                if x[1] is True:
                                                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "range" method returns the blue node(s) above.')
                                                elif x[1] is False:
                                                        t = str(x[0]).replace("[", "").replace("]", "")
                                                        if t == "":
                                                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "range" method returns: ' + str(returned))
                                                        else:
                                                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "range" method returns: ' + str(returned) + '. The nodes with the following keys are highlighted in blue: ' + t + '.')
                                        else:
                                                self.draw(blueX=k, blueRange=(k[0], k[1]))
                                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "range" method returns: ' + str(returned) + ' The nodes whose keys are in the range [' + str(k[0]) + ', ' + str(k[1]) + '] are in blue.')
                                        return
                                else:
                                        self.draw(blueX=k, blueRange=(k[0], k[1]))
                                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='You have not implemented a "range" method in your BST class. The nodes whose keys are in the range [' + str(k[0]) + ', ' + str(k[1]) + '] are in blue.')
                                return
                        except ValueError:
                                return
                
                # search
                k = self.get_key()
                if type(k) == float or type(k) == int:
                        returned = self.BST.search(k)
                        self.update_return(returned, "BST.search(" + str(k) + ") returns: ")
                        x = self.process_returned(returned)
                        if x[1] is True:
                                self.draw(blueX = x[0])
                                self.canvas.create_text(self.w*0.5, self.h-345, anchor=S, text='Your "search" method returns the blue node(s) above.')
                        else:
                                self.draw(blueX=[k])
                                self.canvas.create_text(self.w*0.5, self.h-345, anchor=S, text='Your "search" method returns: ' + str(returned) + '.')
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Tip: Search for a range of keys by entering two numbers, e.g. "0, 100".')
                        return
        
        def minimum(self):
                returned = self.BST.minimum()
                self.update_return(returned, "BST.minimum() returns: ")
                x = self.process_returned(returned)
                self.draw(blueX = x[0])
                if x[1] is True:
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "minimum" method returns the blue node(s) above.')
                else:
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "minimum" method returns: ' + str(returned) + '.')
        
        def maximum(self):
                returned = self.BST.maximum()
                self.update_return(returned, "BST.maximum() returns: ")
                x = self.process_returned(returned)
                self.draw(blueX = x[0])
                if x[1] is True:
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "maximum" method returns the blue node(s) above.')
                else:
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "maximum" method returns: ' + str(returned) + '.')
        
        def floor(self):
                k = self.get_key()
                if type(k) == float or type(k) == int:
                        returned = self.BST.floor(k)
                        self.update_return(returned, "BST.floor(" + str(k) + ") returns: ")
                        x = self.process_returned(returned)
                        self.draw(blueX = x[0])
                        if x[1] is True:
                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "floor" method returns the blue node(s) above.')
                        else:
                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "floor" method returns: ' + str(returned) + '.')
        
        def ceiling(self):
                k = self.get_key()
                if type(k) == float or type(k) == int:
                        returned = self.BST.ceiling(k)
                        self.update_return(returned, "BST.ceiling(" + str(k) + ") returns: ")
                        x = self.process_returned(returned)
                        self.draw(blueX = x[0])
                        if x[1] is True:
                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "ceiling" method returns the blue node(s) above.')
                        else:
                                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Your "ceiling" method returns: ' + str(returned) + '.') 
        
        def size(self):
                try:
                        k = self.get_key()
                        returned = str(self.BST.size(k))
                        self.update_return(returned, "BST.size(" + str(k) + ") returns: ")
                        if k:
                                self.draw(from_here_on=k)
                        elif self.BST.root:
                                self.draw(from_here_on=self.BST.root.key)
                except TypeError:
                        returned = str(self.BST.size())
                        self.update_return(returned, "BST.size() returns: ")
                        if self.BST.root:
                                self.draw(from_here_on=self.BST.root.key)
                self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Count the number of blue nodes to check if your "size" method returns the correct count.')
        
        def rank(self):
                k = self.get_key()
                if type(k) == float or type(k) == int:
                        self.draw(blueRange = (None, k))
                        returned = self.BST.rank(k)
                        self.update_return(returned, "BST.rank(" + str(k) + ") returns: ")
                        self.canvas.create_text(self.w*0.5, self.h-320, anchor=S, text='Count the number of blue nodes to check if your "rank" method returns the correct count.')
                        self.update_return(returned, "BST.rank(" + str(k) + ") returns: ")

        def selection(self):
                k = self.get_key()
                if type(k) == float or type(k) == int:
                        returned = self.BST.selection(k)
                        self.update_return(returned, "BST.selection(" + str(k) + ") returns: ")         
        
        def key_pressed(self, event):
                if event.char == "q":
                        print ('Pressing "q" quits the program.')
                        self.window.destroy()
                
        def quit(self):
                self.window.destroy()

if __name__ == "__main__":
        # CREATE YOUR BST CLASS INSTANCE
        myBST = BST()
        
        # FEED YOUR TREE WITH INITIAL DATA USING "INSERT"
        myBST.insert(7.3, "seven")
        myBST.insert(-1, "three")
        myBST.insert(9, "nine")
        myBST.insert(5, "five")
        myBST.insert(8.7, "eight")

        myGUI = GUI(myBST)
        mainloop()
