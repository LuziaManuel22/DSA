class BinaryTreeNode:
  # Create a node
  def __init__(self, data, newvalue):
    self.data = data
    self.newvalue=newvalue
    self.leftChild = None
    self.rightChild=None

   
def insert(root,key, newValue):
    # Insert a node
    #if binary search tree is empty, make a new node and declare it as root
    if root is None:
        root=BinaryTreeNode(key, newValue)
        return root
    #binary search tree is not empty, so we will insert it into the tree
    #if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if key<root.data:
        root.leftChild=insert(root.leftChild,key,newValue)
    else:
        #if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild=insert(root.rightChild,key, newValue)
    return root


def search(self,key):
    #Condition 1
    if key==self.key:
        return self
    #Condition 3
    elif key <self.key:
        return self.left.search(key) if self.left else None
    # Condition 4
    else:
        return self.right.search(key) if self.right else None



def inorder(root):# Inorder traversal
#if root is None,return
        if root==None:
            return
#traverse left subtree
        inorder(root.leftChild)
#traverse current node(root)
        print(root.data)
#traverse right subtree
        inorder(root.rightChild)   


root= None
root= insert(root,15, 12)
root= insert(root,10, 13)
root= insert(root,25, 14)
root= insert(root,6, 15)
root= insert(root,14, 17)
root= insert(root,20, 20)
root= insert(root,60, 34)
print("")
print("searching the number 14.")
print(root.search(14))
print("")
print("searching the number 22.")
print(root.search(22))
print("")
print("Printing values of binary search tree in Inorder Traversal.")
inorder(root)

""" 
root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
 """
