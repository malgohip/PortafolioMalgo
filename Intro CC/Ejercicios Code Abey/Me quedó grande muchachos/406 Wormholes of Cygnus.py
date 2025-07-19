def find_heist_and_getaway(settlement_count, connections):
    from collections import defaultdict, deque
    
    # Step 1: Initialize graph data structures
    degree = [0] * settlement_count
    graph = defaultdict(dict)
    
    # Step 2: Parse connections and build graph
    for line in connections:
        a, b, w = map(int, line.split())
        degree[a] += 1
        degree[b] += 1
        graph[a][b] = w
        graph[b][a] = w
    
    # Step 3: Find vertices with odd degrees
    odd_vertices = [i for i in range(settlement_count) if degree[i] % 2 == 1]
    
    # Step 4: Check connectivity of the graph
    def is_connected():
        visited = [False] * settlement_count
        def bfs(start):
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
        
        # Find a starting point that has edges
        start = next((i for i in range(settlement_count) if degree[i] > 0), -1)
        if start == -1:
            return True  # No edges in the graph, considered connected
        
        bfs(start)
        # Check if all nodes with edges are visited
        return all(visited[i] for i in range(settlement_count) if degree[i] > 0)
    
    if not is_connected():
        raise ValueError("The graph is not connected.")
    
    # Step 5: Determine "heist" and "getaway" settlements
    if len(odd_vertices) == 0:
        # Eulerian Circuit (pick any two nodes with edges)
        non_zero_degree_nodes = [i for i in range(settlement_count) if degree[i] > 0]
        if len(non_zero_degree_nodes) > 1:
            return non_zero_degree_nodes[0], non_zero_degree_nodes[1]
        else:
            raise ValueError("Not enough vertices with edges to determine heist and getaway.")
    elif len(odd_vertices) == 2:
        # Eulerian Path (return the two odd degree vertices)
        return tuple(sorted(odd_vertices))
    else:
        # More than 2 odd degree vertices means no valid Eulerian Path or Circuit
        raise ValueError("The graph does not have an Eulerian path or circuit.")
    
# Example input data
input_data = """10
0 1 19
0 2 18
0 3 10
0 4 19
0 5 18
0 6 17
0 7 19
0 8 10
0 9 19
1 2 19
1 3 12
1 4 15
1 5 18
1 6 14
1 7 18
1 8 14
1 9 11
2 3 17
2 4 19
2 5 11
2 6 18
2 7 18
2 8 19
2 9 13
3 4 15
3 5 15
3 6 10
3 7 13
3 8 10
3 9 14
4 5 13
4 6 16
4 7 17
4 8 19
4 9 19
5 6 14
5 7 13
5 8 11
5 9 19
6 7 16
6 8 14
6 9 19
7 8 15
7 9 11
8 9 12"""

# Parsing input data
lines = input_data.strip().split('\n')
settlement_count = int(lines[0])
connections = lines[1:]

# Finding heist and getaway settlements
heist, getaway = find_heist_and_getaway(settlement_count, connections)
print(heist, getaway)