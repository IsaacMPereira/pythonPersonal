from collections import deque

# Implementação do algoritmo BFS
def bfs(graph, start):
    # Fila para manter os nós a serem explorados
    queue = deque([start])
    # Conjunto para manter os nós visitados
    visited = set([start])
    
    # Enquanto a fila não estiver vazia
    while queue:
        # Retira o primeiro nó da fila
        node = queue.popleft()
        print(node, end=" ")  # Exibe o nó visitado

        # Para cada vizinho do nó atual
        for neighbor in graph[node]:
            # Se o vizinho ainda não foi visitado
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Definindo o grafo como um dicionário
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

# Chamando a função BFS com o nó inicial 'A'
bfs(graph, 'A')

