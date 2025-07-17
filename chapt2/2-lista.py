class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def create_node(self, value):
        return Node(value)

    def prepend(self, value):
        node = self.create_node(value)
        node.next =  self.head
        self.head = node


# CRIAÇÃO DA LISTA

lista_encadeada = LinkedList() # Lista vazia

lista_encadeada.prepend(35)

print(lista_encadeada.head.value)

lista_encadeada.prepend(42)

print(lista_encadeada.head.value)


