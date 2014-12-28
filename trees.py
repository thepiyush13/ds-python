 
# Binary search tree in python 
# implements basic binary tree data structure
import random
# temporary stack class for variable
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
# main binary search tree calss
class BST():
  def __init__(self,val = None):
    self.left = None
    self.right = None
    self.data = val
    
  def insert(self,val):
    if self.isEmpty():
      self.data = val
    elif (self.data > val):
      if (self.left is None):
        self.left = BST(val)
      else:
        self.left.insert(val)
    else:
      if(self.right is None):
        self.right = BST(val)
      else:
        self.right.insert(val)
      
  
  def __str__(self, depth=0):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    "*depth) + str(self.data)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret
  def isEmpty(self):
    return self.left == self.right == self.data == None
    
  def delete(self,node):
    return false

def generate_bst():
  t = BST()
  i=0
  while(i<10):
    t.insert(random.randrange(1,100))
    i= i +1
  return t

# maximum value in binary tree
# Logic : traverse through all the left nodes and get the max value 
# pass this max value and now traverse all right nodes
# at the end of it, return max_val 
def max_in_bst(node,max_val):
  if node:
    if (node.data > max_val):
      max_val = node.data
    max_val = max_in_bst(node.left,max_val)
    max_val = max_in_bst(node.right,max_val)
  return max_val

# max in binary tree without recursion
# first traverse all left node while pushing right node to stack 
# once end of left nodes are reached , get last enetered value from stack
# this will be a new node so repeat above process till max value is found
def max_in_bst_no_rec(node):
  max_val = node.data
  s = Stack()
  while(node):
    if(node.data > max_val):
      max_val = node.data
    if(node.left and node.left.data > max_val):
      max_val = node.left.data
    if(node.right and node.right.data > max_val):
      max_val = node.right.data
    # right node , we will traverse it later
    if(node.right):
      s.push(node.right)
    
    if(node.left):
      # keep going left
      node = node.left
    else:
      # end of left node , time to get last right node
      if(s.isEmpty()):
        node = None
      else:
        node = s.pop()
  return max_val
  
# t = BST()
t = generate_bst()
print t
# vmax = t.data
# x = max_in_bst(t,vmax)
x = max_in_bst_no_rec(t)
print 'max value',x


  
  