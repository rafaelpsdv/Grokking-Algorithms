from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    queue = deque()
    queue += graph[name]
    verified = []
    while queue:
        person = queue.popleft()
        if person_is_seller(person):
            print(f'{person} é um vendedor de manga!')
            return True
        else:
            queue += graph[person]
            verified.append(person)
    return False
    

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


search('you')
   