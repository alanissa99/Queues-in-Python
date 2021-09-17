from linkedQFile import LinkedQ

if __name__=="__main__":
    que=LinkedQ()

    order=input('Vilken ordning ligger korten i? ')
    order=order.split()
    order=[ int(x) for x in order]
    

    for i in range(len(order)):
        que.enqueue(order[i])
    
    
    output=[]
    while que.isEmpty()==False:
        que.enqueue(que._First.data)
        trash=que.dequeue()                  #when moving my first card to the back with enqueue, it still has a copy in the first element, therefore i throw it away here
        output.append(que.dequeue())
        

    print('De kommer ut i denna ordning:', *output)


