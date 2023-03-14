class TreeNode:    # classe para guardar um no da arvore
    #construtor
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild


    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:                
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):        
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)


#percorre a arvore em ordem
def inorder(self, current_node):
    #visita subarvore a esquerda
    if current_node.left_child:
        self.inorder(current_node.left_child)
    #imprime o valor da raiz
    print(current_node.key)
    #visita subarvore a direita
    if current_node.right_child:
        self.inorder(current_node.right_child)


if __name__ == '__main__':

    T = BinarySearchTree()
    T.put(43, 9.12)
    T.put(34, 5.12)
    T.put(36, 6.134)
    T.put(102, 123.09)
    T.put(87, 5.12)
    T.get(39)
    print("The value is :", T.root.payload)
    T.get(102)
    print("The value is :", T.root.rightChild.payload)
    print('Tree root key: ', T.root.key)
    print('Tree root value: ', T.root.payload)
    print ("traversal in order:" )
    T.put(13, 12.01)
    T.put(12, 45.33)
    T.get(13)
    print("The value is :", T.root.leftChild.payload)
    T.get(15)
    print("The value is :", T.root.leftChild.payload)
    print ("traversal in order:" )


