import numpy
import random

class Node:
        def __init__(self, key_, value_):
                self.key = key_
                self.value = value_
                self.left = None
                self.right = None
                self.parent = None

class BST:
        def __init__(self):
                self.root = None
        
        # cannot insert repeated keys
        # in case of a repeated key, value will be updated
        def insert(self, k, v):
                # create a node
                new_node = Node(k, v)
                # tree is not empty
                if self.root:
                        p = self.root
                        while p:
                                if p.key == k:
                                        p.value = v
                                        return
                                last = p
                                if k > p.key:
                                        p = p.right
                                elif k < p.key:
                                        p = p.left
                        if k < last.key:
                                new_node.parent = last
                                last.left = new_node
                        else:
                                new_node.parent = last
                                last.right = new_node
                # tree is empty 
                else:
                        self.root = new_node
        
        def inorder(self):
                print "In-order: ", 
                self.r_inorder(self.root)
                print "Done!"
        
        def r_inorder(self, p):
                if p:
                        self.r_inorder(p.left)
                        print p.key,
                        self.r_inorder(p.right)


        def search(self, k):
                p = self.root
                while True:
                        if k==p.key:
                                print k, p.value
                                return p.key
                        if k>p.key:
                                if p.right==None:
                                        print "There is no", k,"key!"
                                        return
                                else:
                                        p = p.right
                        if k<p.key:
                                if p.left==None:
                                        print "There is no", k,"key!"
                                        return
                                else:
                                        p = p.left
        def search_node(self, k):
                p = self.root
                while True:
                        if k==p.key:
                                print k, p.value
                                return p
                        if k>p.key:
                                if p.right==None:
                                        print "There is no", k,"key!"
                                        return
                                else:
                                        p = p.right
                        if k<p.key:
                                if p.left==None:
                                        print "There is no", k,"key!"
                                        return
                                else:
                                        p = p.left
        def leaves(self):
                self.num_leaf = 0
                self.leaves_real(self.root)
                return self.num_leaf
                
        def leaves_real(self, cur_node):
                #if both children are present, we have to check for their children as well
                if cur_node.left != None and cur_node.right != None:
                        self.leaves_real(cur_node.left)
                        self.leaves_real(cur_node.right)
                #if there is a left child we have to go down that avenue
                elif cur_node.right == None and cur_node.left != None:
                        self.leaves_real(cur_node.left)
                #if there is a right child we have to go down that avenue
                elif cur_node.left == None and cur_node.right != None:
                        self.leaves_real(cur_node.right)
                #this else is when a node has no children, we then add one to num_leaf
                else:
                        self.num_leaf += 1
                        return
                        
                

        def minimum(self):
                min1 = self.root
                while True:
                        if min1.left==None:
                                print min1.key,"is the min,", min1.value, "is its value"
                                return min1.key
                
                        else:
                                min1 = min1.left

        def maximum(self):
                max1 = self.root
                while True:
                        if max1.right==None:
                                print max1.key,"is the max,", max1.value, "is its value"
                                return max1.key
                
                        else:
                                max1 = max1.right


        ### I did my floor and ceiling weirdly. I wanted to see if I could do them without looking
        ### up how to do it online. They are complicated, but they work!
        def floor(self, k):
                p=self.root
                least = None
                while True:
                        if k==p.key:
                                if p.left:
                                        return p.left.key
                                elif least:
                                        return least.key
                                else:
                                        return p.key
                        elif k>p.key and not p.right:
                                return p.key
                        elif k>p.key:
                                if p.right and k>p.right.key:
                                        p=p.right
                                elif p.right:
                                        a=p.right
                                        if a.left and (k>a.left.key or k==a.left.key):
                                                least=p
                                                p=a.left
                                        elif a.left and k<a.left.key:
                                                least=p
                                                p=a.left
                                        else:
                                                return p.key
                                else:
                                        if least and (least.key>p.key):
                                                return least.key
                                        else:
                                                return p.key
                        elif p.left and k<p.key:
                                p=p.left
                        else:
                                if least:
                                        return least.key
                                else:
                                        print "Error: Key is not in tree"
                                        return

        def ceiling(self, k):
                p=self.root
                least = None
                while True:
                        if k==p.key:
                                if p.right:
                                        a=p.right
                                        if a.left:
                                                p=a.left
                                        else:
                                                return p.right.key
                                elif least:
                                        return least.key
                                else:
                                        return p.key
                        elif k<p.key and not p.left:
                                return p.key
                        elif k<p.key:
                                if p.left and k<p.left.key:
                                        p=p.left
                                elif p.left:
                                        a=p.left
                                        if a.right and (k<a.right.key or k==a.right.key):
                                                least=p
                                                p=a.right
                                        elif a.right and k>a.right.key:
                                                least=p
                                                p=a.right
                                        else:
                                                return p.key
                                else:
                                        if least and (least.key<p.key):
                                                return least.key
                                        else:
                                                return p.key
                        elif p.right and k>p.key:
                                p=p.right
                        else:
                                if least:
                                        return least.key
                                else:
                                        print "Error: Key is not in tree"
                                        return

        def delete(self, k):
                node = self.search_node(k)
                if node.parent == None:
                        del node
                elif node.left and node.right:
                        temp = node.right
                        while True:
                                if temp.left:
                                        temp = temp.left
                                else:
                                        break
                        if node.parent.left is node:
                                temp.right = node.right
                                temp.left = node.left
                                temp.parent.left = None
                                node.parent.left = temp
                                del temp
                        else:
                                temp.right = node.right
                                temp.left = node.left
                                temp.parent.left = None
                                node.parent.right = temp
                                del temp

                        del node
                elif node.left:
                        if node.parent.left is node:
                                node.parent.left = node.left
                        else:
                                node.parent.right = node.left
                        del node
                elif node.right:
                        if node.parent.left is node:
                                node.parent.left = node.right
                        else:
                                node.parent.right = node.right
                        del node
                else:
                        if node.parent.left is node:
                                node.parent.left = None
                        else:
                                node.parent.right = None
                        del node
                print myBST1.inorder()
                
                

myBST1 = BST()
for i in range(15):
        key = random.randint(0,100)
        print "insert ", key
        myBST1.insert(key, "test")

### TEST SUITES
myBST1.leaves()

myBST1.insert(50,1)
myBST1.insert(20,1)
myBST1.insert(15,1)
myBST1.insert(79,1)
myBST1.insert(82,1)

myBST1.search(50)
myBST1.search(20)
myBST1.search(15)
myBST1.search(79)
myBST1.search(82)

myBST1.minimum()
myBST1.maximum()

print 50, myBST1.floor(50)
print 75, myBST1.floor(75)
print 60, myBST1.floor(60)
print 30, myBST1.floor(30)
print 10, myBST1.floor(10)
print 95, myBST1.floor(95)

print 50, myBST1.ceiling(50)
print 75, myBST1.ceiling(75)
print 60, myBST1.ceiling(60)
print 30, myBST1.ceiling(30)
print 10, myBST1.ceiling(10)
print 95, myBST1.ceiling(95)

myBST1.delete(50)
myBST1.delete(20)

myBST1.inorder()




