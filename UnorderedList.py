#########################
#Unordered list
#########################
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        curent = self.head
        maxLen = 10
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
            if count = maxLen:
                current.

        return count

    def __str__(self):
        return str("[", self.head, "]")
    #I don't feel that that's correct... ^

    def append(self, item):
        current = self.head
        temp = Node(item)
        while current != None:
            current = current.getNext()

        current.setNext(temp)

    def insert(self, pos, item):
        current = self.head
        previous = None
        index = 0
        temp = Node(item)

        while current != None and index < pos:
            previous = current
            current = current.getNext()
            index += 1
    
        if pos == 0:
            temp.setNext(self.head)
            self.head = temp      
        else:
            if current == None:
                previous.setNext(temp)
            else:
                temp.setNext(current)
                previous.setNext(temp)
    def index(self, item):
        current = self.head
        found = False
        index = 0

        while current != None and not found:
            if current.getData() != item:
                index +=1
                current = current.getNext()
            else:
                found = True

        if found:
            return index
        else:
            return "Not Found"

    def pop(self):
        current = self.head
        previous = None

        if current == None:
            return "No item in list"

        while current.getNext() != None:
            previous = current
            current = current.getNext()

        previous.setNext(None)
        return current.getData()
