# Detect loop in a linked list

# Given a linked list, check if the linked list has loop or not. Below diagram shows a linked list with a loop. 

class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
        
    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )
    
    def detectLoop ( self ) :
        temp = self.head
        while ( temp ) :
            if temp.flag == 1 :
                print ( " loop detected " )
                break
            temp.flag = 1
            temp = temp.next

llist = LinkedList()
llist.add ( 1 )
llist.add ( 2 )
llist.add ( 1 )
llist.add ( 1 )
llist.add ( 5 )
llist.add ( 1 )
llist.head.next.next.next = llist.head
llist.detectLoop()