from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visitados = set([start])

    while queue: #Equanto a lsita não estiver vazia
        node = queue.popleft()
        print(node, end=" ")

        for vizinho in graph[node]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                queue.append(vizinho)
    print("\n")
    
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

bfs(graph, 'A')