from collections import deque 

class UndirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)
        self.adjacency_list[w].append(v)
    
    def is_bipartite(self, start_vertex):
        # Create a double ended queue to store the vertices to be explored
        queue = deque([start_vertex])
        # Initialize the colors of the vertices and assign a color to the start vertex
        colors = [None] * self.num_vertices
        colors[start_vertex] = 0
        # Perform BFS
        while queue:
            vertex = queue.popleft()
            for neighbor in self.adjacency_list[vertex]:
                # If the neighbor has not been colored yet assign it the opposite color
                if colors[neighbor] is None:
                    colors[neighbor] = 1 - colors[vertex]
                    queue.append(neighbor)
                # If the neighbor has the same color as the vertex, then the graph is not bipartite
                elif colors[neighbor] == colors[vertex]:
                    return False
                # If the neighbor has the same color as the vertex continue
                else: 
                    continue
        return True


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
    print(f"\nBipartite?: {UG.is_bipartite(0)}")