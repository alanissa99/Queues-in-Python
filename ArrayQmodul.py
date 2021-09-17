from arrayQFile import ArrayQ 

if __name__=="__main__":
    que=ArrayQ()

    order=input('Vilken ordning ligger korten i? ')
    order=order.split()
    order=[ int(x) for x in order]      #All elements in my variable "order" become integers. (Previously were strings)
    

    for i in range(len(order)):         #Entering all the numbers into the array
        que.enqueue(order[i])
    
    
    output=[]
    while que.isEmpty()==False:
        que.enqueue(que._front)       #Moves the first card to the back
        trash=que.dequeue()             #when moving my first card to the back with enqueue, it still has a copy in the first element, therefore i throw it away here
        output.append(que.dequeue())    #Taking out the second card
        

    print('De kommer ut i denna ordning:', *output)

    # The order is 7 1 12 2 8 3 11 4 9 5 13 6 10