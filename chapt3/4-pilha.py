class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.top = self.create_node(None)
    
    def create_node(self, value):
        return Node(value)

    def push(self, value):
        node = self.create_node(value)
        node.prev =  self.top
        self.top = node
    
    def pop(self):
        mem = self.top.value
        self.top = self.top.prev
        return mem


pilha = Stack()
print(pilha.top.value)
pilha.push(5)
print(pilha.top.value)
teste = pilha.pop()
print(teste)
print(pilha.top.value)




