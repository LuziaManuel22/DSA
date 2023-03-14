class TreeNode:     #criar node da arvore de busca
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key # chave
        self.payload = val  #valor
        self.leftChild = left #filho a esquerda
        self.rightChild = right #filho a direita
        self.parent = parent # no pai

    def hasLeftChild(self): #verifica se tem filho a esquerda
        return self.leftChild

    def hasRightChild(self): #verifica se tem filho a direita
        return self.rightChild

    def isLeftChild(self): #verifica se e filho a esquerda de alguem
        return self.parent and self.parent.leftChild == self #tem q ter no pai e ser filho dele a esquerda

    def isRightChild(self): #verifica se e filho a direita de alguem
        return self.parent and self.parent.rightChild == self #tem q ter no pai e ser filho dele direita

    def isRoot(self): #verifica se e no raiz
        return not self.parent #raiz n pode ter pai

    def isLeaf(self): #verifica se e no folha
        return not (self.rightChild or self.leftChild) #folha n tem filho a esquerda nem a direita

    def hasAnyChildren(self): #verifica se no tem algum filho
        return self.rightChild or self.leftChild #basta ter um filho a esquerda ou direita

    def hasBothChildren(self): #verifica se tem ambos os filhos
        return self.rightChild and self.leftChild # deve ter filho a esquerda e a direita

    def updateNodeData(self,key,value,lc,rc): #actualiza dados do no
        self.key = key #new key
        self.payload = value #new value
        self.leftChild = lc #new leftchild
        self.rightChild = rc # new rightchild
        if self.hasLeftChild(): #e pai do seu novo filho a esquerda 
            self.leftChild.parent = self
        if self.hasRightChild():  #e pai do seu novo filho a direita 
            self.rightChild.parent = self

class BinarySearchTree: # implement the class binarySearchTree
    def __init__(self): #construtor
        self.root = None
        self.size = 0

    def length(self): #retorna numero de nos da tree
        return self.size

    def insert(self,key,val): #vai ver se a arvore ja tem raiz, se n tiver entao sera criado e sera a raiz
        if self.root: #se raiz existe
            self._insert(key,val,self.root)#add o elemento apartir da raiz(achar posicao certa)
        else:
            self.root = TreeNode(key,val)# se n tem raiz cria novo no raiz
        self.size = self.size + 1 #incrementa o numero de nos

    def _insert(self,key,val,currentNode):#se ja existe raiz chama essa funcao auxiliar para inserir na arvore de busca
        if key < currentNode.key: #se a key e menor olha na subarvore a esquerda
            if currentNode.hasLeftChild(): #se ja tem filho a esquerda, chama funcao recursiva
                   self._insert(key,val,currentNode.leftChild) #chama para inserir
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)#encontrou a posicao certa
        else:#aqui a key e maior ou igual, entao subarvore da direita
            if currentNode.hasRightChild():#se ja tem filho a direita chama funcao auxiliar para inserir
                   self._insert(key,val,currentNode.rightChild)
            else:#encontrou posicao certa
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def search(self,key): #buscar elemento com key
        if self.root:#se tem raiz
            res = self._search(key,self.root)# chama funcao recursiva auxiliar de busca
            if res:                
                return res.payload # se retorna elelmto diferente de none
            else:
                return None
        else:
            return None

    def _search(self,key,currentNode): # funcao auxiliar para busca de elemento na tree      
        if not currentNode: #se no corrente n existe n existe elemento
            return None #retorna none
        elif currentNode.key == key: #se a chave do elemento igual a chave de busca, entrou
            return currentNode #retorna  valor
        elif key < currentNode.key: #se a chave menor q o no
            return self._search(key,currentNode.leftChild) #buscar na subarvore esquerda
        else:
            return self._search(key,currentNode.rightChild) #buscar na subarvore direita

    #percorre a arvore em ordem
    def inorder(self, currentNode):
        if currentNode.leftChild:#visita subarvore a esquerda
            self.inorder(currentNode.leftChild)
            print(currentNode.key)#print a raiz
        if currentNode.rightChild:#visita subarvore a direita
            self.inorder(currentNode.rightChild)

        
    def delete(self,key):
      if self.size > 1:
         currentNode = self._search(key,self.root)
         if currentNode:
             self.remove(currentNode)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)
  

    def height(self, root):
        if root is None:
            return 0
        leftHeight= self.height(root.leftChild)
        rightHeight=self.height(root.rightChild)
        max_height= leftHeight
        if rightHeight>max_height:
            max_height = rightHeight
        return max_height+1

            
if __name__  == '__main__':
    T = BinarySearchTree()
    T.insert(43, 9.12)
    T.insert(34, 5.12)
    T.insert(36, 6.134)
    T.insert(102, 123.09)
    T.insert(87, 5.12)
    print("") 
    print ("traversal in order:")
    T.inorder(T.root)
    print("Height of the binary tree is:")
    print(T.height(T.root))
    print("The key is 39 and the value is :", T.search(39))
    print("") 
    print("")
    print("The key is 102 and the value is :", T.search(102))
    print("") 
   #print('Tree root key: ', T.root.key)
   #print('Tree root value: ', T.root.payload)
    print("")
   # T.delete(43)
    T.delete(34)
    T.delete(36)
    T.delete(102)
    T.delete(87)
   # T.delete(43)
    """print("") 
    print("")
    print("The key is 13 and the value is  :",  T.search(13))
    print("") 
    print("")
    print("The key is 15 and the value is :", T.search(15))
    print ("traversal in order:") """
    T.inorder(T.root)
  


