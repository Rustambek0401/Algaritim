class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkenList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def push(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data
    def insert(self,prev_node,new_data):
        if prev_node is None:
            print("EROR")
        new_data = Node(new_data)
        new_data.next = prev_node.next
        prev_node.next = new_data

    def append(self, new_data):
        new_data = Node(new_data)
        if self.head is None:
            self.head = new_data
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_data

    def delete(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev


a = Node(3)
s = Node(6)
d = Node(2)
f = Node(4)
g = Node(5)
link = LinkenList()
link.head = a
a.next = s
s.next = f
f.next = d
d.next = g
link.push(11)
link.push(22)
link.push(33)
link.insert(a,111)
link.insert(d,222)
link.insert(g,333)
link.append(999)
link.append(888)
link.append(777)
link.printlist()
link.delete()
link.printlist()