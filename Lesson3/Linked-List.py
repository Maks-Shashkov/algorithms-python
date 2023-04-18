class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class List_1:
    def __init__(self, data):
        new_node = Node(data)
        self.start_node = new_node

    def print_l(self):
        if self.start_node is None:
            print("список пустой")
            return
        n = self.start_node
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print("\n")

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node

    def delete_start(self):
        if self.start_node is None:
            print("список пустой")
            return
        self.start_node = self.start_node.next

    def delete_and(self):
        n = self.start_node
        while n.next.next is not None:
            n = n.next
        n.next = None

    def reverse_list(self):
        prev_node = None
        current_node = self.start_node
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.start_node = prev_node



l1 = List_1(4)
l1.insert_start(3)
l1.insert_start(2)
l1.insert_end(5)
l1.delete_and()
l1.delete_start()
l1.print_l()
l1.reverse_list()
l1.print_l() # выводит: 4 3 2 1
