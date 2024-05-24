from typing import Optional

class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

    def __lt__(self, other: 'Node') -> bool:
        return self.key < other.key
    
    def __gt__(self, other: 'Node') -> bool:
        return self.key > other.key
    
    def __eq__(self, other: 'Node') -> bool:
        return self.key == other.key

class BST:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def isEmpty(self) -> bool:
        return self.root is None

    def insert(self, key: int) -> Node:
        new_node = Node(key)
        if self.isEmpty():
            self.root = new_node
            return new_node
        
        current = self.root
        parent = None
        
        while current is not None:
            parent = current
            if new_node < current:
                current = current.left
            else:
                current = current.right
        
        new_node.parent = parent
        
        if new_node < parent:
            parent.left = new_node
        else:
            parent.right = new_node
        
        return new_node

    def search(self, key: int) -> Optional[Node]:
        current = self.root
        while current is not None and current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def max(self, node: Optional[Node] = None) -> Optional[Node]:
        if node is None:
            node = self.root
        if node is None:
            return None
        
        while node.right is not None:
            node = node.right
        
        return node

    def min(self, node: Optional[Node] = None) -> Optional[Node]:
        if node is None:
            node = self.root
        if node is None:
            return None
        
        while node.left is not None:
            node = node.left
        
        return node

    def inOrderPredecessor(self, key: int) -> Optional[Node]:
        """
    Finds the in-order predecessor (node visited before) for a key in the BST.

    1. Search for the target node.
    2. If not found, return None (no predecessor).
    3. If the node has a left child:
       - Predecessor is the rightmost node in the left subtree (max of left subtree).
    4. Otherwise, traverse parents:
       - While a parent exists and the current node is its left child:
          - Move up the parent chain (current node becomes the parent).
       - If parent becomes None (root reached), there's no predecessor on the right side.
       - Otherwise, the parent is the predecessor (visited before the current node).
    """
        node = self.search(key)
        if node is None:
            return None
        
        if node.left is not None:
            return self.max(node.left)
        
        parent = node.parent
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.parent
        return parent

    def inOrderSuccessor(self, key: int) -> Optional[Node]:
    #      """
    # Finds the in-order successor (node visited after) for a key in the BST.

    # 1. Search for the target node.
    # 2. If not found, return None (no successor).
    # 3. If the node has a right child:
    #    - Successor is the leftmost node in the right subtree (min of right subtree).
    # 4. Otherwise, traverse parents:
    #    - While a parent exists and the current node is its right child:
    #       - Move up the parent chain (current node becomes the parent).
    #    - If parent becomes None (root reached), there's no successor on the left side.
    #    - Otherwise, the parent is the successor (visited after the current node).
    #     """
        
        node = self.search(key)
        if node is None:
            return None
        
        if node.right is not None:
            return self.min(node.right)
        
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.parent
        return parent

    def preOrderPredecessor(self, key: int) -> Optional[Node]:
        """
    Finds the pre-order predecessor (node visited before) for a key in the BST.

    1. Search for the target node.
    2. If not found, return None (no predecessor).
    3. Handle cases based on node's position:
       - Root: No predecessor in pre-order.
       - Left child: Parent is the predecessor (visited earlier in pre-order).
       - Right child: Predecessor is rightmost node in left subtree.
    """
        node = self.search(key)
        if node is None:
            return None

        parent = node.parent
        if parent is None:
            return None

        if parent.left == node:
            return parent

        if parent.right == node:
            # Find the rightmost node of the left subtree of the parent
            sibling = parent.left
            while sibling.right is not None:
                sibling = sibling.right
            return sibling

        return None


    def preOrderSuccessor(self, key: int) -> Optional[Node]:
        node = self.search(key)
        if node is None:
            return None
        
        if node.left is not None:
            return node.left
        
        if node.right is not None:
            return node.right
        
        parent = node.parent
        while parent is not None and (node == parent.right or parent.right is None):
            node = parent
            parent = parent.parent
        
        if parent is not None:
            return parent.right
        return None

    def postOrderPredecessor(self, key: int) -> Optional[Node]:
        """
    This method finds a potential neighbor for a node with a specific 'key' 
    considering a modified tree traversal. It's not a true predecessor 
    in a strict post-order traversal (left, right, root).

    1. Search for the target node and check for children.
    2. If it has a right child, return the largest node in the right subtree.
    3. If it has a left child, return the largest node in the left subtree.
    4. If no children, traverse parents:
       - If target is left child and parent has left child, no neighbor found.
       - If target is right child and parent has left child, return parent's left child.
    5. If no valid neighbor found after parents, return None.
        """
        node = self.search(key)
        if node is None:
            return None
        
        if node.right:
            return self.max(node.right)
        
        if node.left:
            return self.max(node.left)
        
        parent = node.parent
        while parent and (node == parent.left or parent.left is None):
            node = parent
            parent = parent.parent
        
        if parent is None:
            return None
        else:
            return parent.left

    def postOrderSuccessor(self, key: int) -> Optional[Node]:
        #This code searches a tree for a value and finds the next value that would be
        # visited if you travelled through the tree left-to-right, then bottom-to-top.
        node = self.search(key)
        if node is None:
            return None

        parent = node.parent
        if parent is None:
            return None

        if parent.right == node or parent.right is None:
            return parent

        if parent.left == node:
            # Find the leftmost node of the right subtree of the parent
            sibling = parent.right
            while sibling.left is not None:
                sibling = sibling.left
            return sibling

        return None

