import array


class ArrayInt:
  # constructor, set up the array
  def __init__(self, size=20):
    if size < 1:
      size = 20 #copied & edited from last lab
    self.size = size 
    self.lastIndex = 0
    self.count = -1
    self.theArray = array.array('i', [0] * size)  #blanks in textbook are 0s here for python.

# adds a new value to the tail of the queue, wrapping if necessary. 
#if there is no room to add a new value, calls the resize( ) method.

  def addTail(self, value):
    if self.size == self.lastIndex:
        self.resize()
    if :
        #wrapping?
    else
        self.theArray.append(value)
    
    self.count += 1
    return self


  def getHead(self): #for lols.     ... #dr.majchrzak if you actually read these i am sorry.
    head = self.thisArray[self.count]
    return head
  
#saves the value at the head of the queue, updates it to remove access to
#that value, and returns the saved value, wrapping if necessary. 
# If the queue is empty throws
#an exception. (For C++ and C#, use the message: Array is empty in removeHead
  def removeHead(self):
    self.count -= 1
    return self.getHead()
  
  #returns an array containing the contents of the array from index 0 to
#size-1. This is for debugging purposes and to verify that wrapping is working properly.
  def dumpArray(self):

    return self
  


#creates a new array twice as large and copies the elements to it. This should
#properly deal with situations where there has been wrapping and the tail is at an index less
#than the head. Note, this is not a simple exercise where you can copy index 0 of the old
#array to index 0 of the new array and so forth. You will need to end up after copying with
#the head at index 0 and tail appropriately located. There are several ways to accomplish
#this. 

  def resize(self):

    return self




#returns a string listing the elements from head to tail. This should
#properly deal with situations where there has been wrapping and the tail is at an index less
#than the head. 
  def listQueue(self):

    return self
  



#returns true when the double ended queue is empty, false otherwise.
  def isEmpty(self):
    return self




# adds a new value at the head. Wraps if necessary. This should
#not overwrite data that was previously in the queue. If the array is full, calls resize( ) to
#double the array and copy the data as needed.
  def addHead(self):

    return self




# saves the value at the tail of the queue, updating the queue to remove
#access to the item at the tail, and returns the saved value. Wraps if necessary. If the queue
#is empty, throws an exception. (For C++ and C#, use the message: Array is empty in
#removeTail) 
  def removeTail(self):

    return self
  

    '''
    How could you implement a stack using your double ended queue? Use this concept to list a
    provided set of numbers in reverse order. More specifically, add a method to your Deque class
    called thinkSolve which takes two arguments, an array of integers and the number of elements in
    the list. It instantiates a new deque, adds the integers to the new deque in their original order, then
    removes the integers from the new deque in reverse order and adds them to the original deque
    upon which thinkSolve was called.
    '''
