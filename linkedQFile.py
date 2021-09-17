class LinkedQ:
    def __init__(self):             #My class has two private attributes, a first and a last
        self._First=None
        self._Last=None

    def enqueue(self,x):
        new=Node(x)                 #I create a node
        new.data=x                  #I then put the desired data into the node
        if self._First==None:        #Just like in the array class, if there are no nodes in the que, then the incoming node is both first and last
            self._First=new
            self._Last=new
        else:                       #Otherwise, the new node is sent to the end of the que
            self._Last.next=new
            self._Last=new

    def dequeue(self):              #We remove the first node in the que while redirecting the "First" attribute
        x=self._First.data
        self._First=self._First.next
        if self._First==None:
            self._Last=None
        return x

    def isEmpty(self):
        if self._First==None:
            return True
        else:
            return False

    def remove(self,x):

        pointer=self._First    #Starting at the first node

        if self._First==None:  #If its an empty que, nothing happens   
            pass             

        elif pointer.data==x: #If the first node is the match, then the first node is removed by redirecting self.First
            self._First=self._First.next
            if pointer.next!=None:  #This is used to check if there are other nodes in the que that match
                self.help_remove(x)

        else:                 #If its not an empty que, and the first node doesnt match, it comes here
            self.help_remove(x)

    def help_remove(self,x):        #This function was created so that i dont write the same code twice
        pointer=self._First          #Start off at the first node
        while pointer.next!=None:   #Continue until the end of the que
    
            if pointer.next.data==x:    #If the next node matches, then the "next" pointer is redirected
                if pointer.next==self._Last: #Special case: If pointer.next is the final node, since pointer.next.next isnt defined
                    self._Last=pointer
                    self._Last.next=None

                else:                   #"next" pointer is redirected here
                    pointer.next=pointer.next.next
            
            else:               
                pointer=pointer.next    #Goes to the next node





class Node:                        
    def __init__(self, x, next=None): # My class has two attributes, data which stores incoming data and a next which works as a pointer
        self.data=x
        self.next=next


#test=LinkedQ()
#test.enqueue(1)
#test.enqueue(2)
#test.enqueue(3)

#test.remove(2)
#test.remove(1)
#test.remove(4)
#test.remove(1) #Tom kö!
#test.remove(3)
