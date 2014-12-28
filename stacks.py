 
from random import randrange
import copy
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        if(len(self.items)>0):
            return 0
        else:
            return 1
    
    def push(self,item):
        self.items.append(item)
       
    def pop(self):
        return self.items.pop()
    def length(self):
        return len(self.items)
# PRINTING STACKS
def print_stack(stack):
    y = []
    while(not stack.is_empty()):
        y.append(stack.pop())
    print y    
    return 
# GENRATE STACK DATA
def create_stack():
    s = Stack()
    for i in range(1,10):
        s.push(randrange(10) )
    return s
# STACKS: Q1 : CUSTOM FUNCTION LIST

def balance_symbol(str):
    if(str is None):
        return None
    s_left = Stack()
    s_right = Stack()
    
    
    for l in str:
        
        if( (l=='(' ) or (l=='{' ) or (l=='[' )    ):
            s_left.push(l)
        elif (l==')'):
              if( s_left.is_empty() and s_left.pop()!='('):
              	return 'UNBALANCED'
        elif (l=='}'):
              if(s_left.is_empty() and s_left.pop()!='{'):
              	return 'UNBALANCED'
        elif (l==']'):
              if(s_left.is_empty() and s_left.pop()!='['):
              	return 'UNBALANCED'        
        
        
    return 'BALANCED'
    
# Q 5: o(1) Stack 
class minStack:
    def __init__(self):
        self.minS = Stack()
        self.items = []
    def push(self,item):
        self.items.append(item)
        if self.minS.length() !=0:
            prev = self.minS.pop()
            cur = item
            if(cur>prev):
                self.minS.push(prev)

            else:
                self.minS.push(cur)

        else:
            self.minS.push(item)
           
    def is_empty(self):
        if(len(self.items)>0):
            return 0
        else:
            return 1
    def pop(self):
        return self.items.pop()    

    def getMinimum(self):
        return self.minS.pop()

# Q8: pallindrom in ababab....abXbababa....ba x is the middle point
def palindrome_string(string):
    if(not string):
        return None
    middle = False
    t = Stack()
    for s in string:
        if(s=='x'):
            middle = True
        elif(middle is True):
            top = t.pop()
            if(top != s):
                return False
        else:
            t.push(s)
    return True
# reverse a list 
def rev_str(string):
    t = Stack()
    r = ''
    for s in string:
        t.push(s)
    while(not t.is_empty()):
        r = r + t.pop()
    return r
        
        
            
# print palindrome_string('hi2x3ih')
print rev_str('abcdef')

