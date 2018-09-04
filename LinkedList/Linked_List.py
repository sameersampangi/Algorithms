'''
Implementing an LinkedList, creating two classes, one class to implement the node functionality
and other class to implement the LinkedList functionality
'''

__author__="Sameer Sampangi"

class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.length = 0
        #self.head = None


    def setNext(self,next):
        self.next=next

    def getNext(self):
        return self.next

    def getData(self):
        return self.data

    def setData(self,data):
        self.data=data


class Linked_List(object):

    def __init__(self):
        self.head = None

    def insert_begin(self,data):
        node = Node(data)
        if self.head==None:
            self.head = node
        else:
            current = self.head
            self.head=node
            self.head.setNext(current)

    def insert_position(self,data,position):
        if position == 0:
            self.insert_begin(data)




    def insert_end(self,data):
        node=Node(data)
        current = self.head
        while(current.getNext()!= None):
            current=current.getNext()
        current.setNext(node)

    def display(self):
        current = self.head
        while current !=None:
            print(current.getData())
            current=current.getNext()





a= Linked_List()
a.insert_begin(9)
a.insert_end(12)
a.insert_end(22)
a.insert_begin(54)
a.display()




#
# a = Node(9)
# a.setNext(12)
# a.getNext()
# a.setNext(13)
# print(a.getData())
# print(a.getNext())
