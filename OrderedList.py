from  NodeLi import *
class OrderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        print(self.head ==None)
    def size(self):
        count = 0
        current = self.head
        while  current != None:
            count += 1
            current = current.get_next()
        print(count)

    def search(self,item):
        current = self.head
        found = False
        while current != None and not False:
            if current.get_data ==item:
                found = True
            else:
                current = current.get_next()

    def Remove(self,item):
        current = self.head
        prev = None
        found = False
        while current !=None and not found:
            if current.get_data() == item:
                found = True
            else:
                prev = current
                current = current.get_next()
        if prev ==None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())


    def add(self,item):
        current = self.head
        prev = None
        Stop = False
        while current !=None and not Stop:
            if current.get_data() >item:
                Stop = True
            else:
                prev = current
                current = current.get_next()
        temp = Node(item)
        if prev == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(prev.get_next())
            prev.set_next(temp)

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not False:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    Stop = True
                else:
                    current = current.get_next()
        return found


li = OrderedList()
li.add(30)
li.add(10)
li.add(60)
li.add(3)
li.size()
li.is_empty()
