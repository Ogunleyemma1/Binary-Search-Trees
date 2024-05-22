from typing import Any

class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __lt__(self, other):
        if other is None:
            return False
        return self.key < other.key
    
    def __gt__(self, other):
        if other is None:
            return False
        return self.key > other.key
    
    def __eq__(self, other):
        if other is None:
            return False
        return self.key == other.key
    
    def __ge__(self, other):
        if other is None:
            return False
        return self.key >= other.key
    
    def __le__(self, other):
        if other is None:
            return False
        return self.key <= other.key

class BST:
    def __init__(self) -> None:
        self.root = None

    def isEmpty(self) -> bool:
        #Method returns true if the root is none
        return self.root is None

    def insert(self, key: int) -> Node:
       #Create a new node and pass its key value
       newNode = Node(key)

       #write a conditional statement to set new node as root if tree is empty
       if self.isEmpty():
           self.root = newNode
       else:
           #Else, it recursively insert the new node into the three
            self.insertRecursive(self.root, newNode)

        #Return the newly inserted node
       return newNode 
     
    #---------------------------------------------------------------------------------------------------------------------------
    #Implementing a recurrsive helper function for insertion
    def insertRecursive(self, currentNode: Node, newNode: Node) -> None:

        #Implementing a conditional statement when the new code is less than the current node to the LHS
        if newNode < currentNode:

            #if there is no node in the LHS set the new node to LHS, else create a new node by repeating recursive function
            if currentNode.left is None:
                currentNode.left = newNode
                newNode.parent = currentNode
            else:
                self.insertRecursive(currentNode.left, newNode)

        #Implement a conditional statement for when newNode >= current node        
        else:
            #if the RHS of current node is none then set newNode as current RHS
            if currentNode.right is None:
                currentNode.right = newNode
                newNode.parent = currentNode
            else:
                self.insertRecursive(currentNode.right, newNode)
    #--------------------------------------------------------------------------------------------------------------------------------------
        
    def search(self, key: int) -> Node:
        return self.searchRecursive(self.root, key)
    
    #------------------------------------------------------------------------------------------------------------------------------------------------
    #Implementing a helper function for the search recussive
    def searchRecursive(self, currentNode: Node, key: int) -> Node:

        #Implementing a conditional statement to return current node if the current node is none or the current node key equals key
        if currentNode is None or currentNode.key == key:
            return currentNode
        
        if key < currentNode.key:
            return self.searchRecursive(currentNode.left, key)
        
        else:
            return self.searchRecursive(currentNode.right, key)
        
    #------------------------------------------------------------------------------------------------------------------------------------------------
    def max(self, node: Node = None) -> Node:
        #implementing a condition to start from the root if no node is provided
        if node is None:
            node = self.root

        #Implementing a condition to return none is there is no node in the tree
        if node is None:
            return None
        
        #Implementing a loop that goes round tree and return the max number
        while node.right is not None:
            node = node.right
        
        return node

    def min(self, node: Node = None) -> Node:
        #implementing a condition to start from the root if no node is provided
        if node is None:
            node = self.root

        #Implementing a condition to return none is there is no node in the tree
        if node is None:
            return None
        
        #Implementing a loop that goes round tree and return the max number
        while node.left is not None:
            node = node.left
        
        return node

    def inOrderPredecessor(self, key: int) -> Node:
        
        #Find the node given the key
        node = self.search(key)
        if node is None:
            return None
        
        #Finding the maximum of the left subtree if it exist
        if node.left is not None:
            return self.max(node.left)
        
        # if there is no left subtree, proceed to find the nearest parent for which the node is in the right subtree
        nearestParent = node.parent
        while nearestParent is not None and node == nearestParent.left:
            node = nearestParent
            nearestParent = nearestParent.parent

        return nearestParent


    def inOrderSuccessor(self, key: int) -> Node:
        #Find the node given the key
        node = self.search(key)
        if node is None:
            return None
        
        #Finding the minimum of the right subtree if it exist
        if node.right is not None:
            return self.max(node.right)
        
        # if there is no left subtree, proceed to find the nearest parent for which the node is in the left subtree
        nearestParent = node.parent
        while nearestParent is not None and node == nearestParent.right:
            node = nearestParent
            nearestParent = nearestParent.parent

        return nearestParent

    def preOrderPredecessor(self, key: int) -> Node:
        
        # Find the node with the given key
        node = self.search(key)
        if node is None:
            return None
        
        # If the node has a left child, the predecessor is the rightmost node in the left subtree
        if node.left is not None:
            return self.max(node.left)
    
        # If the node has no left child, traverse up the tree using parent pointers
        # Until we find a node that is the right child of its parent, and return the parent
        ancestor = node.parent
        while ancestor is not None and node == ancestor.left:
            node = ancestor
            ancestor = ancestor.parent

        return ancestor

    def preOrderSuccessor(self, key: int) -> Node:
         #Find the node which the key is given
        node =self.search(key)
        if node is None:
            return None
        
        #if the node has a left child, the left child is the preorder successor
        if node.left is not None:
            return node.left
        
        #if the node has no left child but has a right child, the right child is the preorder successor
        if node.right is not None:
            return node.right
        
        #if the node has no children, travel up using parent pointers until we find a node
        #that is the left child of its parent, and the parent will be the pre-order succesor
        ancestor = node.parent
        while ancestor is not None and (ancestor.right is None or node == ancestor.right):
            node = ancestor
            ancestor = ancestor.parent

        #if we found such an ancestor, return its right child (if it exist)
        if ancestor is not None:
            return ancestor.right
        
        #if we didnt find any ancestor, return none
        return None

    def postOrderPredecessor(self, key: int) -> Node:
         # Find the node with the given key
        node = self.search(key)
        if node is None:
            return None
    
        # If the node is the root or has a left child, there's no postorder predecessor
        if node == self.root or node.left is not None:
            return None
    
        # If the node is a right child, traverse up the tree using parent pointers
        # Until we find a node that is the left child of its parent, and return the parent
        ancestor = node.parent
        while ancestor is not None and node == ancestor.right:
            node = ancestor
            ancestor = ancestor.parent

        return ancestor

    def postOrderSuccessor(self, key: int) -> Node:
        node = self.search(key)
        if node is None:
            return None
        
        #If the node is the root, it has no postorder succesor
        if node == self.root:
            return None
        
        parent = node.parent
        #if the node is a left child, check the right subtree of the parent or the parent itself
        if parent is not None and node == parent.left:
            if parent.right is not None:
                return self.min(parent.right)
            else:
                return parent
        
        #If the node is a right child, the parent is the successor
        if parent is not None and node == parent.right:
            return parent
        
        return None
    
