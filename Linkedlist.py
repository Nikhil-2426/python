class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None


class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class sLinkedlist:
    def __init__(self) :
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval=printval.nextval
    def AtBeginning(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self. headval
        self.headval=NewNode            
list=sLinkedlist()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.AtBeginning("Sun")
list.listprint()                                   





