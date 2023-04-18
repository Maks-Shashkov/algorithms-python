
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color = "RED"  # начальный цвет новых нод - RED


class RedBlackTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        new_node = Node(value)
        self.root = self._add_node_helper(self.root, new_node)
        self.root.color = "BLACK"  # корень всегда должен быть черным

    def _add_node_helper(self, current_node, new_node):
        if current_node is None:
            return new_node

        if new_node.value < current_node.value:
            current_node.left = self._add_node_helper(current_node.left, new_node)
        else:
            current_node.right = self._add_node_helper(current_node.right, new_node)

        # балансировка дерева
        if self._is_red(current_node.right) and not self._is_red(current_node.left):
            current_node = self._rotate_left(current_node)
        if self._is_red(current_node.left) and self._is_red(current_node.left.left):
            current_node = self._rotate_right(current_node)
        if self._is_red(current_node.left) and self._is_red(current_node.right):
            self._flip_colors(current_node)

        return current_node

    def _is_red(self, node):
        if node is None:
            return False
        return node.color == "RED"

    def _rotate_left(self, node):
        new_node = node.right
        node.right = new_node.left
        new_node.left = node
        new_node.color = node.color
        node.color = "RED"
        return new_node

    def _rotate_right(self, node):
        new_node = node.left
        node.left = new_node.right
        new_node.right = node
        new_node.color = node.color
        node.color = "RED"
        return new_node

    def _flip_colors(self, node):
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"

def print_tree(node, level=0, prefix=' '):
    if node is not None:
        print_tree(node.right, level + 1, prefix='│   ')
        print(prefix + '└── ' + str(node.value))
        print_tree(node.left, level + 1, prefix='│   ')

# создание дерева
root = Node(7)
root.left = Node(3)
root.right = Node(18)
root.left.left = Node(1)
root.left.right = Node(5)
root.right.left = Node(12)
root.right.right = Node(22)

# вывод дерева в консоль
print_tree(root)
