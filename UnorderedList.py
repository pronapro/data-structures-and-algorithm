from  NodeLi import *
class UnorderedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head ==None
    def add(self,item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current !=None:
            count += 1
            current = current.get_next()
        print(count)
    def search(self,item):
        current = self.head
        found = False
        while current !=None and not found :
            if current.get_data() != item:
                current =current.get_next()
            else:
                found = True
        return found

    """def Remove(self,item):
        current = self.head
        prev =None
        found = False
        while not found:
            if current.get_data() ==item:
                found = True
            else:
                prev = current
                current = current.get_next()
        if prev ==None:
            self.head = current.get_next()
        else:
            prev.set_next(current.get_next())"""
    def Remove(self,item):
        prev = None
        current = self.head
        found = False
        while current !=None and not found:
            if current.get_data() == item:
                found = True
                if prev ==None:
                    self.head = current.get_data()
                else:
                    prev.set_next(current.get_next())
            else:
                prev = current
                current = current.get_next()








li = UnorderedList()
li.add(50)
li.add(5)
li.add(20)
li.add(60)
li.add(500)
#li.size()
li.search(5)
li.is_empty()
#li.output_list()
li.Remove(60)
li.Remove(20)
li.size()
