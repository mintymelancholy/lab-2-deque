import array


class Deque:
  # constructor, set up the array
  def __init__(self, size=20):
    if size < 1:
      size = 20 #copied & edited from last lab
    self.size = size 
    self.left = -1 #head is left +1   #doing it like this to match the wrapping assignment. i still don't get it.
    self.right = 0 #tail is right
    self.count = 0
    #self.lastIndex = 0 #should lastIndex just be the tail? ... yeeeahh.. probly. nvm yes fs
    self.theArray = array.array('i', [0] * size)  #blanks in textbook are 0s here for python.



# adds a new value to the tail of the queue, wrapping if necessary. 
#if there is no room to add a new value, calls the resize( ) method.

  def addTail(self, value): # "tail points to the next location to add" page52

    # chewed through a whole coffee stirrer for this one jesus christ lol. figured it out tho
    if self.right >= self.size:
      self.theArray[0] = value #first wrapped
      self.right = 1 

    elif self.size == self.count: # or self.right == self.size
      self.resize(newSize = self.size * 2)
      self.theArray[self.right] = value  #self.right should be one after count. ... but then i have a 0. 
        
      self.right += 1

    else: #self.size != self.count and self.right < self.size:
      self.theArray[self.right] = value     #NOT APPEND!!!!!!!! MAKES ARRAY 21!!!
      self.right += 1
    
   # else:  #THE CULPRIT!!! (i think) it isnt elseing with the if its doing both the first if and the else. fixed.

    self.count += 1
    return self


  #def getHead(self): #for lols.   ... #dr.majchrzak if you actually read these i am sorry. i do believe this function will actually be useful as well though.
  # # head = self.theArray[self.le
   # return head
  
#saves the value at the head of the queue, updates it to remove access to
#that value, and returns the saved value, wrapping if necessary. 
# If the queue is empty throws an exception. (For C++ and C#, use the message: Array is empty in removeHead

  def removeHead(self):
    #head = self.getHead() #needs to be BEFORE left incriment ...(i do not know how to spell that.)
    
    
    if self.count <= 0:
      raise IndexError('Array is empty in removeHead')
    elif self.size <= self.left + 1:
      self.left = 0
      head = self.theArray[self.left] 
    else:
      self.left += 1
      head = self.theArray[self.left] 
    self.count -= 1
    self.listArray = self.theArray
    return head #old head, its gone now.
  
  

  #returns an array containing the contents of the array from index 0 to  SIZE -1
  # #LIESSSSSS!!!!! DOESN'T WANT YOU TO RETURN AN ARRAY IT WANTS A STRING. !!
#This is for debugging purposes and to verify that wrapping is working properly.
  def dumpArray(self):
    dumpList = ''
    for i in self.theArray:
      dumpList += str(i) + ' '
    return dumpList
  


#creates a new array twice as large and copies the elements to it. This should
#properly deal with situations where there has been wrapping and the tail is at an index less
#than the head. Note, this is not a simple exercise where you can copy index 0 of the old
#array to index 0 of the new array and so forth. You will need to end up after copying with
#the head at index 0 and tail appropriately located. There are several ways to accomplish
#this. 

  def resize(self, newSize):
    newArray = array.array('i', [0] * newSize)

    if self.right <= self.left + 1 : 
      headI = self.left + 1
      tailI = self.right 

      accu = self.size - headI
      newtail = 0
      while headI < self.size and accu > 0:
        newArray[newtail] = self.theArray[headI] # just i makes the values backwards.
        newtail += 1
        accu -= 1
        headI += 1
        
      #while tailI > 0:
      for i in range (tailI):
        
        newArray[newtail] = self.theArray[i]
        newtail += 1
         #
        #tailI -= 1

      #while ??? < tailI:  #self.left + 1 is actual head idx not the iterative headI
    #  for i in range (tailI):
     #   newArray[newArray.size - i] = self.theArray[i]
        #tailI -= 

    #all copies fine.  its adding the new ones thats the issue.
    else:
      for value in range(self.right):
        newArray[value] = self.theArray[value]


    self.right = self.count #also since count is number of used idexes not index numbers,  
    #count is one more than the index of the last number so the +1 was +2-ing. kira's fault >:(   /joking
  
    self.theArray = newArray 
    self.size =  newSize  

    self.left = self.size - 1
    return self



#returns a string listing the elements from head to tail. This should
#properly deal with situations where there has been wrapping and the tail is at an index less
#than the head. 
  def listQueue(self):
    listArray = array.array('i', [0] * self.count)

    if self.right <= self.left + 1 :  #modded from my resize func.
      headI = self.left + 1
      tailI = self.right 

      accu = self.size - headI
      newtail = 0
      while headI < self.size and accu > 0:
        listArray[newtail] = self.theArray[headI] 
        newtail += 1
        accu -= 1
        headI += 1

      for i in range (tailI):
        listArray[newtail] = self.theArray[i]
        newtail += 1 #


    else:
      for value in range(self.right):
        listArray[value] = self.theArray[value]


    list = ''
    for i in listArray: #modded from dumparray
      list += str(i) + ' '

    return list
  



#returns true when the double ended queue is empty, false otherwise.
  def isEmpty(self):
    if self.count <= 0:
      empty = True
    else:
      empty = False
    return empty




# adds a new value at the head. Wraps if necessary. This should
#not overwrite data that was previously in the queue. If the array is full, calls resize( ) to
#double the array and copy the data as needed.

  def addHead(self, value):

    #modded from addtail
    if self.left >= self.size:
      self.theArray[0] = value #test doesnt check if this works so idk yet
      self.left = 1 

    elif self.left < 0:
      #wrap
      self.left = self.size - 1
      self.theArray[self.left] = value
      self.left -= 1


    elif self.size == self.count: 
      self.resize(newSize = self.size * 2)#test doesnt check if this works so idk yet
      #if self.left == -1:
        #self.left = self.size - 1
        #self.theArray[self.left] = value
    #  else:
        #self.left -= 1
      self.theArray[self.left] = value  
      self.left -= 1
      #self.theArray[self.left] = value  
      

    else:
      self.theArray[self.left] = value     
      self.left -= 1

    self.count += 1
    return self




# saves the value at the tail of the queue, updating the queue to remove
#access to the item at the tail, and returns the saved value. Wraps if necessary. If the queue
#is empty, throws an exception. (For C++ and C#, use the message: Array is empty in
#removeTail) 
  def removeTail(self):
      
    if self.count <= 0:
      raise IndexError('Array is empty in removeTail')
    elif self.size == self.right:
      self.right = 0 #this is probly wrong
      self.right -= 1
    else:
      self.right -= 1
      if self.right < 0:
       self.right = self.size - 1

      
    tail = self.theArray[self.right]
    self.count -= 1
    self.listArray = self.theArray
    return tail
  

    '''
    How could you implement a stack using your double ended queue?
    Use this concept to list a provided set of numbers in reverse order. 
    More specifically, add a method to your Deque class called thinkSolve which takes two arguments,
    an array of integers and the number of elements in the list. 
    It instantiates a new deque, adds the integers to the new deque in their original order, then
    removes the integers from the new deque in reverse order and adds them to the original deque
    upon which thinkSolve was called.
    '''



  def solveThink(self, nums, count):
    newDeque = Deque()

    for i in range(count):
      newDeque.addTail(nums[i])

    for i in range(count):
      val = newDeque.removeTail()
      self.addTail(val)

    return self
  



    '''
    How could you implement a stack using your double ended queue? Use this concept to list a
    provided set of numbers in reverse order. More specifically, 
    add a method to your Deque class
    called thinkSolve
            #wrong^ main.py wants solveThink not thinkSolve
       which takes two arguments, an array of integers and the number of elements in
    the list. 
    It instantiates a new deque, adds the integers to the new deque in their original order, then
    removes the integers from the new deque in reverse order and adds them to the original deque
    upon which thinkSolve was called.
    '''
