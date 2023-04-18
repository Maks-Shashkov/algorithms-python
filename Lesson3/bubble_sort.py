class Node:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node
            current_node.next_node = new_node
            new_node.prev_node = current_node

    def bubble_sort(self):
        if self.head is None:
            return

        end = None
        while end != self.head.next_node:
            current_node = self.head
            while current_node.next_node != end:
                next_node = current_node.next_node
                if current_node.data > next_node.data:
                    current_node.data, next_node.data = next_node.data, current_node.data
                current_node = next_node
            end = current_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next_node
        print()

# Пример использования
linked_list = DoublyLinkedList()
linked_list.add_node(5)
linked_list.add_node(2)
linked_list.add_node(8)
linked_list.add_node(1)

print("Список до сортировки:")
linked_list.print_list()

linked_list.bubble_sort()

print("Список после сортировки:")
linked_list.print_list()