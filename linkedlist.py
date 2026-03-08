class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    class linkedlist:
     def __init__(self):
       self.head=None
    def display(self):
            if self.head is None:
                print('linked list is empty')
            else:
                temp=self.head
                while temp:
                    print(temp.data,"-->",end=" ")
                    temp=temp.next
                    l=linkedlist()
                    n=node(10)
                    head=n
                    second=node(20)
                    third=node(30)
                    n.next=second
                    n.next=third

