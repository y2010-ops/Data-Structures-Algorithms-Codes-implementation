class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        count = 0
        while curr.next != None:
            count += 1
            curr = curr.next
        return count

    def display(self):
        e = []
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            e.append(curr_node.data)
        print(e)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            last_node_d = last_node.data
            cur_node = cur_node.next
            cur_node_d = cur_node.data
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1



my_list = Linked_list()
# my_list.display()
my_list.append(2)
my_list.append(1)
my_list.append(5)
my_list.append(3)
my_list.append(4)
my_list.display()
# my_list.length()
print(my_list.get(9))
my_list.erase(4)
my_list.display()