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
        # plan:

        # create a variable that holds the current node in the 
        # tree 

        # create a while loop that will traverse the tree and 
        # terminate if the value was not found 

            # if target > current_node.value traverse to the right 
            # if target < current_node.value traverse to the left 
            # if target == current_node.value return True 

        current_node = self

        while current_node:
            if target > current_node.value:
                current_node = current_node.right
            elif target < current_node.value:
                current_node = current_node.left
            else:
                return True 

        return False 

    # Return the maximum value found in the tree
    def get_max(self):
        # plan:

        # create a current node variable initialized to the current root 

        # create a max variable that will collect all the node values 
        # to the right of the root nodes.

        # create a while loop that will terminate if current_node 
        # equals None 

        # modify max variable to current_node's value 
        # modify current node to current_node.right 

        current_node = self
        max_value = 0

        while current_node:
            max_value = current_node.value 
            current_node = current_node.right

        return max_value


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # divide and conquer method 

        # the next node can be separated between self.right and self.left 
        # will need to create a recursive case that will call both next nodes 
        # in the tree and terminate once the passed node is None.

        # plan:
        # create a function that will be used as the recursive helper 
        # for the passed in cb function.
            # base case: if passed in node is None return nothing 

            # else 
                # pass current node's value into the cb function
                # next call the helper function on the right and left 
                # nodes of the current node 

        def recursive_function_helper(current_node):
            if current_node == None:
                return 

            else:
                cb(current_node.value) 
                recursive_function_helper(current_node.right)
                recursive_function_helper(current_node.left)

        recursive_function_helper(self)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        ## first attempt 
        # I will not use a stack to recursively 
        # print the nodes using in-order depth first traversal 
        # as I feel that the implementation is most likely the same 
        # as my for_each method helper function implementation 

        # plan:
        # stop traversal if the passed in node is None 

        # else:
        # recursively call the self.in_order_print() with first the left node
        # and then the right node. 
        # remember that within the middle you have to print(node.value) 
        # the following is the correct permuation for in-order depth first traversal 
        # <self.in_order_print(node.left)>
        # <print(node.value) >
        # <self.in_order_print(node.right)>

        if node == None:
            return 
        else:
            self.in_order_print(node.left) 
            print(node.value)
            self.in_order_print(node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue call discovered 
        # initialize the queue with the root node of the tree 

        # create a while loop that will terminate once the discovered
        # queue is empty (discovered.len() == 0) 
            # remove the oldest node in the queue discovered.dequeue() and
            # print the value 

            # if node.left != None: enqueue node.left 
            # if node.right != None: enqueue node.right
        
        discovered = Queue() 
        discovered.enqueue(node)

        while discovered.len() > 0:
            explored = discovered.dequeue() 
            print(explored.value)

            if explored.left != None:
                discovered.enqueue(explored.left) 
            if explored.right != None:
                discovered.enqueue(explored.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # similar to in-order depth first search except that 
        # you need to order the recursive steps and print statement 
        # as:
        # print(node.value) 
        # <pre_order_dft(node.left)>
        # <pre_order_dft(node.right)>

        if node == None:
            return 
        else:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # similar to in-order depth first search except that 
        # you need to order the recursive steps and print statement 
        # as:
        # <post_order_dft(node.left)>
        # <post_order_dft(node.right)>
        # print(node.value) 

        if node == None:
            return 
        else:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)

arr = []
cb = lambda x: arr.append(x)

new_tree = BinarySearchTree(3)
new_tree.insert(2)
new_tree.insert(5)
new_tree.insert(1)
# print(new_tree.right.value)
# print(new_tree.contains(0))
# print(new_tree.get_max())
# new_tree.for_each(cb)
# print(arr)
# new_tree.in_order_print(new_tree)
# new_tree.bft_print(new_tree)

bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print(bst)
