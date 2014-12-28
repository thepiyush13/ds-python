import random

# Create a queue and implement it 
class Queue:
  def __init__(self):
    self.data = []
  def enqueue(self,item):
    # put at end of the queue
    self.data.insert(0,item)
  def dequeue(self):
    # pop from last element
    return self.data.pop()
  def isEmpty():
    # length of current queue
    return self.data == []
  def size(self):
    return len(self.data)

def create_queue():
  x = Queue()
  for i in range(0,10):
    # x.enqueue(random.randrange(0,10))
    x.enqueue(i)
  return x
def print_q(item):
  x = ''
  for i in range(item.size()):
    x = x+ ' '  +str(item.dequeue())
  print x 
# reverse the queue 
def reverse_q(item):
  x = []
  for i in range(item.size()):
    x.append(item.dequeue())
  j = len(x)-1
  while(j>0):
    print x[j]
    j = j-1

myq = create_queue()
# print_q(myq)
reverse_q(myq)

  
    