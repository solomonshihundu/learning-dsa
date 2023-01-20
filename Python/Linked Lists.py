#Node class whose objects will store the data and associated reference
#Defines a default constructor
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

#Class whose objects instantiate as call to create and populate a linkedlist
#Also prints out elements of linkedlist in respective order
#Defines a default constructor to instantiate the head of the node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        print("Node is of Type : ", type(node))
        self.head = node

    def print(self):
        if self.head is None:
            print("LinkedList is Empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head =Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print("LinkedList is Empty")
            return

        itr = self.head
        while itr:   
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            print("LinkedList is Empty")
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


    def print_data(self,data):
        if self.head is None:
            print("LinkedList is Empty")
            return

        itr = self.head
        while itr:   
            if str(itr.data) == data:
                print("Data is : ",data)
                break
            itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at_beginning("Kiwi")
    ll.remove_at(1)
    ll.print_data("orange")
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.insert_after_value("orange","peas")
    ll.insert_after_value("banana","lemon")
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()