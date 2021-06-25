from collections import deque

graph = {}

graph['you'] = ['alice', 'bob', 'claire']

graph['alice'] = ['peggy']
graph['anuj'] = []
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['jonny'] = []
graph['peggy'] = []
graph['thom'] = []


def find_mango_seller(graph):
    search_queue = deque()
    search_queue += graph

    checked = []

    while search_queue:
        person = search_queue.popleft()

        if not person in checked:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                
            checked.append(person)
    
    print('No mango seller found :(')
    return False


def person_is_seller(name):
    return name[0] == 'z'


find_mango_seller(graph)