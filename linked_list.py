  
    
#LINKED LIST CLASS INIT 
class Node:
  def __init__(self):
    self.data = None # contains the data
    self.next = None # contains the reference to the next node

# create a linked list without a cycle    
head = Node()
head.data = 0
current = head

for i in range(1,9):
  new_node = Node()
  new_node.data = i
  current.next = new_node
  current = new_node  

# Printer function for linked list
def printList(head):
  current = head
  print "\r\n---Begin Print---"
  while current.next:
    print current.data
    current = current.next

  print current.data
  print "---End Print---"    


    


    
#CUSTOM FUNCTIONS FOR LINKED LISTS

# creating a function to reverse the linked list 
def reverseList(head):
    current = head
    prev = None
    next = None
    while(current):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head  
#displaying linked list from the end 
def display_list_from_end(head):
    if(not(head)):
        return 
    display_list_from_end(head.next)
    print head.data

#check if given linked list is even or odd 
def odd_or_even(head):
    if(head is None or head.next is None):
        print 'empty'
        return 
    i=0
    while(head.next):
        i = i+1
    if(i%2==0):
        print 'Even list'
    else:
        print 'Odd list'
        
    return 
#function to reverse link list by pair
def revListPair(head):
    cur = head
    while(cur is not None):
        temp = head.next
        head.next = head
        head = temp
        cur = cur.next
    
#COMMANDS TO CALL FUNCTIONS 

printList(head)    
#printList(reverseList(head))
#display_list_from_end(head)
#odd_or_even(head)
#revListPair(head)
printList(head)
    

  
    
    
    
   