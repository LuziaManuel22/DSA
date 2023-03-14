class TreeNode: # classe para guardar um no da arvore
   #construtor
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key=key #chave
        self.payload=val #valor armazenado na chave
        self.left_child=left #filho a esquerda
        self.right_child=right #filho a direita
        self.parent=parent  #no pai

    def has_left_child(self): #verifica se tem filho a esquerda
        #se retornar None n tem
        return self.left_child
    
    def has_right_child(self): #verifica se tem filho a direita
        #se retornar None n tem
        return self.right_child

    def is_left_child(self): #verifica se o no e filho a esquerda de alguem
        #tem q ter um no pai e ser filho a esquerda desse no pai
        return self.parent and self.parent.left_child ==self
    
    def is_right_child(self): #verifica se o no e filho a direita de alguem
        #tem q ter um no pai e ser filho a direita desse no pai
        return self.parent and self.parent.right_child ==self
    
    def is_root(self): #verifica se no e raiz
        #raiz n pode ter pai
        return not self.parent

    def is_leaf(self):#verifica se e folha
        #folha n tem filho a esquerda nem a direita
        return not (self.right_child or self.left_child)

    def has_anyChild(self):#verifica s etem algum filho
        #basta ter um filho a esquerda ou a direita
        return self.right_child or self.left_child
    
    def has_bothChildren(self): #verifica se os dois tem filhos
        #deve ter filho a esuqerda e a direita
        return self.right_child and self.left_child

    
    #updating the data of the node
    def update_node_data(self, key, value, lc, rc):
        self.key=key       # nova chave
        self.payload=value # novo valor
        self.left_child=lc #novo filho a esquerda
        self.right_child=rc #novo filho a direita



     #implementando a classe BinarySearchTree
class BinarySerachTree:
    #construtor
    def __init__(self):
        self.root = None #criar raiz vazia
        self.size = 0
        
 #retorna o numero de nos da arvor
    def length(self):
        return self.size
    
    #permite usar a funcao built-in len() doo Python
    def  __len__(self):
        return self.size

# esse metodo ira checar s ea arvore ja tem uma raiz 
#se n tiver sera criado um novo node e sera a raiz da arvore
#se a raiz ja existe entao o metodo chama a funcao insert para
#procurar o local certo do elemento na arvore, de forma recursiva

def insert(self, key, val):
    #se a raiz existe
    if self.root:
        #adiciona elemento apartir da raiz(vai achar a posicao certa)
        self.insert(key,val,self.root)
    else:
        #se n tem raiz cria novo no
        self.root =TreeNode(key,val)
        #incrementa o numero de nos
    self.size = self.size + 1

def put(self, key , val, current):#funcao auxiliar recursiva para insercao na arvore de busca
    #se a chave e menor olha na subarvore a a esquerda
    if key < current.key:
        #se ja tem um filho a esquerda dispara funca recursiva
        if current.has_left_child():
            self.put(key,val,current.left_child)
        else:
            #encontrou posicao certa
           current.left_child = TreeNode(key, val, parent=current)

    else:
        #aqui a chave e maior, entao subarvore da direita
        #se ja tem filho a direita dispara funcao recursiva
        if current.has_right_child():
            self.put(key,val,current.right_child)
        else:#encontrou a posicao certa
            current.right_child = TreeNode(key,val,parent=current)

 #agora podemos sobrecarregar o operador colchetes como T[a=123]
 #inserir 123 em [a] como por exemplo

def __setitem__ (self, k, v):
    self.insert(k, v)

#busca pelo elemento com chave
def get(self, key):
    #se arvore tem raiz
    if self.root:
        #dispara funcao recursiva auxiliar de busca
        res= self._get(key, self.root)
        #se retorna elemento dferente de None, pq achou seu elemento
        if res:
            return res.payload #retorna o valor
        else:
            return None
    else:
        return None        
#funcao auxiliar recursiva para busca do elemento na arvore
def _get(self, key, current):
    #se no corrente n existe, n existe elemento
    if not current:
        return None
    #se a chave do elemento igaul a chave de busca, encontrou
    elif current.key == key:
        return current
    #se chave menor q o no
    elif key< current.key:
        #buscar na arvore esquerda
        return self._get(key, current.left_child)
    else:
        #buscar na arvore direita
        return self._get(key, current.right_child)

#agora T[a] para retornar o valor cuja chave e 'a'
def __getitem__(self, key):
    return self.get(key)

#permite utilizar o operador in para realizar a busca
#como em 'a' in T
def __contains__(self, key):
    if self._get(key, self.root):
        return True
    else:
        return False

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

if __name__== '__main__' :

    T =BinarySerachTree()
   
    T= insert(None, 43, 9.12)
    T= insert(34, 5.12)
    T= insert(36, 6.134)
    T= insert(102, 123.09)
    T= insert(87, 5.12)

""" 
    print("")
    print("searching the key 39.")
    T= insert(root,)
    print("searching the key 102.")
    T= insert(root,)
    print("Printing values of binary search tree in Inorder Traversal.")
    inorder(root)
    T= insert(root,13, 12.01)
    T= insert(root,12, 45.33)
    print("")
    print("searching the key 13.")
    T= insert(root,)
    print("searching the key 15.")
    root= insert(root,)
    print("Printing values of binary search tree in Inorder Traversal.")
    inorder(T) """
    


