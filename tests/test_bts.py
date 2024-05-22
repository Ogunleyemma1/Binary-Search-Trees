import pytest
from bts import BST, Node

def create_tree(keys):
    bst = BST()
    for key in keys:
        bst.insert(key)
    return bst

# Test insert function
def test_insert():
    bst = BST()
    bst.insert(5)
    assert bst.root.key == 5
    bst.insert(3)
    assert bst.root.left.key == 3
    bst.insert(7)
    assert bst.root.right.key == 7
    bst.insert(4)
    assert bst.root.left.right.key == 4
    bst.insert(2)
    assert bst.root.left.left.key == 2

# Test search function
def test_search():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.search(5).key == 5
    assert bst.search(4).key == 4
    assert bst.search(8) is None

# Test min function
def test_min():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.min().key == 2

# Test max function
def test_max():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.max().key == 7

# Test inOrderPredecessor function
def test_inOrderPredecessor():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.inOrderPredecessor(5).key == 4
    assert bst.inOrderPredecessor(2) == None
    assert bst.inOrderPredecessor(7).key == 5
    assert bst.inOrderPredecessor(4).key == 3

# Test inOrderSuccessor function
def test_inOrderSuccessor():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.inOrderSuccessor(5).key == 7
    assert bst.inOrderSuccessor(2).key == 3
    assert bst.inOrderSuccessor(7) is None
    assert bst.inOrderSuccessor(4).key == 5

# Test preOrderPredecessor function
def test_preOrderPredecessor():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.preOrderPredecessor(5) is None
    assert bst.preOrderPredecessor(2).key == 3
    assert bst.preOrderPredecessor(7).key == 4
    assert bst.preOrderPredecessor(4).key == 2

# Test preOrderSuccessor function
def test_preOrderSuccessor():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.preOrderSuccessor(5).key == 3
    assert bst.preOrderSuccessor(2).key == 4
    assert bst.preOrderSuccessor(7) is None
    assert bst.preOrderSuccessor(4).key == 7

# Test postOrderPredecessor function
def test_postOrderPredecessor():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.postOrderPredecessor(5).key == 7
    assert bst.postOrderPredecessor(2) == None
    assert bst.postOrderPredecessor(7).key == 3
    assert bst.postOrderPredecessor(4).key == 2

# Test postOrderSuccessor function
def test_postOrderSuccessor():
    bst = create_tree([5, 3, 7, 2, 4])
    assert bst.postOrderSuccessor(5) is None
    assert bst.postOrderSuccessor(2).key == 4
    assert bst.postOrderSuccessor(7).key == 5
    assert bst.postOrderSuccessor(4).key == 3

# Test for an empty tree
def test_empty_tree():
    bst = BST()
    assert bst.isEmpty() == True

# Test for a single node tree
def test_single_node_tree():
    bst = BST()
    bst.insert(5)
    assert bst.isEmpty() == False
    assert bst.min().key == 5
    assert bst.max().key == 5

# Test for a large tree
def test_large_tree():
    bst = create_tree(range(100))
    assert bst.min().key == 0
    assert bst.max().key == 99

# Test for a small tree
def test_small_tree():
    bst = create_tree([5])
    assert bst.min().key == 5
    assert bst.max().key == 5

if __name__ == "__main__":
    pytest.main()