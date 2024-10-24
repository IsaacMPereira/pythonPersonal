import heapq

# Implementação do algoritmo Best-First Search
def best_first_search(graph, start, goal, heuristic):
    # Priority queue (fila de prioridade) para armazenar os nós a serem explorados
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic[start], start))
    
    # Conjunto para rastrear nós visitados
    visited = set()

    while priority_queue:
        # Pega o nó com menor valor de heurística
        _, current_node = heapq.heappop(priority_queue)
        
        # Se o nó atual for o objetivo, termina a busca
        if current_node == goal:
            print(f"Objetivo '{goal}' encontrado!")
            return

        print(f"Visitando: {current_node}")
        visited.add(current_node)

        # Expande os vizinhos do nó atual
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    print("Objetivo não encontrado.")

# Exemplo de grafo como um dicionário
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Função de heurística (estimativa de custo para o objetivo)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 7,
    'E': 2,
    'F': 1
}

# Executando o Best-First Search do nó 'A' até o nó 'F'
best_first_search(graph, 'A', 'F', heuristic)
