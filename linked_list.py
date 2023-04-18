class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)        #making new node and setting self.head as next
        self.head = node    # making new node as self. head

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:    # till there are elements in the node list
            itr = itr.next
        itr.next = Node(data,None)    #creating a new node at the end 

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index <0 or index > ll.get_length():
            raise Exception("not possible")
        if index == 0:
            self.head = self.head.next   #if removing element is first node, make the second node as first node

        itr = self.head
        count = 0
        while itr:
            if count == index-1:    # if index is the node to be deleted , take the node previus to it and create the connection to the next node of the node which is getting deleted
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
    def insert_at(self,index,data):
        if index <0 or index > ll.get_length():
            raise Exception("not possible")
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index -1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count+1

    def print(self):           #utility function to print the output
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr +=str(itr.data) + '--->'
            itr = itr.next
        print(llstr)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(['banana','mango',"grapes",'orange'])
    ll.print()
    
    ll.insert_at(0,"figs")
    ll.print()
         