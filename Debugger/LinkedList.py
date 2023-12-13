from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        newNode = Node(e)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        self.size += 1

    def delete(self, i):
        curr = self.head
        while i > 1: # loop until you're at the one to delete
            curr = curr.getNext()
            i -= 1

        prev = curr.getPrevious()
        post = curr.getNext()
        if prev is None: # if deleting the first element
            self.head = post
        else:
            prev.setNext(post)
        if post is None: # if deleting the last element
            self.tail = prev
        else:
            post.setPrevious(prev)
        self.size -= 1 # decrement size

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        # don't do this
        # while (current != None)
        # while (current)
        while (current.getData() is not None):
        # like saying while (not(current is None))    
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

if __name__ == "__main__":
    lst = LinkedList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    print(lst)
    # lst.delete(2)
    # print(lst)
