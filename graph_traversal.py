from collections import deque 

class UndirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)
        self.adjacency_list[w].append(v)
    
    def bfs(self, start_vertex):
        # Create a double ended queue to store the vertices to be explored
        queue = deque([start_vertex])
        # Create a list to store the vertices that have been visited
        visited = [False] * self.num_vertices
        # While the queue is not empty
        while queue:
            # Get the next vertex to be explored
            vertex = queue.popleft()
            # If the vertex has not been visited
            if not visited[vertex]:
                # Mark it as visited
                visited[vertex] = True
                print(f"Vertex {vertex} is explored")
                
                # Explore its neighbors
                for neighbor in self.adjacency_list[vertex]:
                    queue.append(neighbor)

    def dfs(self, start_vertex):
        # Create a stack to store the vertices to be explored. Recursion can also be used
        stack = [start_vertex]
        # Create a list to store the vertices that have been visited
        visited = [False] * self.num_vertices
        while stack:
            # Get the next vertex to be explored
            vertex = stack.pop()
            # If the vertex has not been visited
            if not visited[vertex]:
                # Mark it as visited
                visited[vertex] = True
                print(f"Vertex {vertex} is explored")
                
                # Explore its neighbors
                for neighbor in self.adjacency_list[vertex]:
                    stack.append(neighbor)


class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

    def bfs(self, start_vertex):
        # Create a double ended queue to store the vertices to be explored
        queue = deque([start_vertex])
        # Create a list to store the vertices that have been visited
        visited = [False] * self.num_vertices
        # While the queue is not empty
        while queue:
            # Get the next vertex to be explored
            vertex = queue.popleft()
            # If the vertex has not been visited
            if not visited[vertex]:
                # Mark it as visited
                visited[vertex] = True
                print(f"Vertex {vertex} is explored")
                
                # Explore its neighbors
                for neighbor in self.adjacency_list[vertex]:
                    queue.append(neighbor)
    
    def dfs(self, start_vertex):
        # Create a stack to store the vertices to be explored. Recursion can also be used
        stack = [start_vertex]
        # Create a list to store the vertices that have been visited
        visited = [False] * self.num_vertices
        while stack:
            # Get the next vertex to be explored
            vertex = stack.pop()
            # If the vertex has not been visited
            if not visited[vertex]:
                # Mark it as visited
                visited[vertex] = True
                print(f"Vertex {vertex} is explored")
                
                # Explore its neighbors
                for neighbor in self.adjacency_list[vertex]:
                    stack.append(neighbor)


if __name__=="__main__":
    UG = UndirectedGraph(6)
    UG.add_edge(0,1)
    UG.add_edge(0,2)
    UG.add_edge(1,2)
    UG.add_edge(2,4)
    UG.add_edge(4,5)
    UG.add_edge(5,3)

    print("\nUndirected Graph:\n")
    for vertex,edges in enumerate(UG.adjacency_list):
        print(f"{vertex}: {edges}")
    print("\nBFS:\n")
    UG.bfs(0)
    print("\nDFS:\n")
    UG.dfs(0)

    DG = DirectedGraph(6)
    DG.add_edge(0,1)
    DG.add_edge(0,2)
    DG.add_edge(1,2)
    DG.add_edge(2,4)
    DG.add_edge(4,5)
    DG.add_edge(5,3)

    print("\nDirected Graph:\n")
    for vertex,edges in enumerate(DG.adjacency_list):
        print(f"{vertex}: {edges}")
    print("\nBFS:\n")
    DG.bfs(0)
    print("\nDFS:\n")
    DG.dfs(0)