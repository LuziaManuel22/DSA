# Tabela Hash sem tratamento de colisões


class Hash:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def funcaohash(self, chave):
          v = int(chave)
          return v%self.tam_max

     def cheia(self):
          return len(self.tab) == self.tam_max

     def imprime(self):
          for i in self.tab:
               print("Hash[%d] = " %i, end="")
               print (self.tab[i])

     def apaga(self, chave):
          pos = self.busca(chave)
          if pos != -1:
               del self.tab[pos]
               print("-> Dado da posicao %d apagado" %pos) 
          else:
               print("Item nao encontrado")

     def busca(self, chave):
          pos = self.funcaohash(chave)
          if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
          if self.tab[pos] == chave: 
               return pos
          return -1

     def insere(self, item):
          if self.cheia():
               print("-> ATENÇÃO Tabela Hash CHEIA")
               return
          pos = self.funcaohash(item)
          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = item
               print("-> Inserido HASH[%d]" %pos)
          else: # se posicao ocupada
               print("-> Ocorreu uma colisao na posicao %d" %pos)             
# fim Classe Hashlinear

tamanhoHash = 7
tab = Hash(tamanhoHash)
print("\n****************************************************")
print("      Tabela HASH Sem Colisões (%d itens) " %tamanhoHash)
print("****************************************************")
for i in range (0,tamanhoHash,1):
     print("\nInserindo elemento %d" %(i + 1));
     item = input(" - Forneca valor numerico inteiro: ")
     tab.insere(item)
item = input("\n - Forneca valor numerico inteiro para buscar: ")
pos = tab.busca(item)
if pos == -1:
     print("Item nao encontrado")
else:
     print("Item encontrado na posicao: ", pos)
item = input("\n - Forneca valor numerico inteiro para apagar: ")
tab.apaga(item)
print("\nImprimindo conteudo")
tab.imprime()
print("\n")