import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # rather simplistic for the first insert since all 
        # one needs to do is check if value is less then or greater 
        # than the input value and place it to the left or right 
        # respectively.

        # How do you insert a value that is two nodes deep in the 
        # tree? 

        # plan: simple solution but only valid for the first right or left 
        # insert.

        # if value < self.value:
            # place the value to the left
        # if value >= self.value:
            # place the value to the right 
        
        # plan: complex insert used for inserting values multiple 
        # children deep.

        # first create a current node variable.

        # create a while loop that will terminate once the current node is 
        # None 

        # place value in the None node spot.

        current_node = self

        while current_node:
            if current_node.value > value:
                if current_node.left == None:
                    current_node.left = BinarySearchTree(value)
                    # breaking points needed to stop infinite loop.
                    break
                else: 
                    current_node = current_node.left
            elif current_node.value <= value:
                if current_node.right == None:
                    current_node.right = BinarySearchTree(value)
                    # breaking points needed to stop infinite loop.
                    break
                else:
                    current_node = current_node.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

new_tree = BinarySearchTree(3)
new_tree.insert(2)
new_tree.insert(5)
new_tree.insert(1)
print(new_tree.right.value)
