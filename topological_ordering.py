class DirectedGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]

    def add_edge(self, v, w):
        self.adjacency_list[v].append(w)

    def topological_sort(self):
        # Initialize the stack and visited list
        stack = []
        visited = [False] * self.num_vertices

         # Perform DFS on each vertex
        for vertex in range(self.num_vertices):
            if not visited[vertex]:
                self._topological_sort_dfs(vertex, visited, stack)

        # Reverse the stack to get the topological ordering
        return stack[::-1]

    def _topological_sort_dfs(self, vertex, visited, stack):
        visited[vertex] = True

        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self._topological_sort_dfs(neighbor, visited, stack)

        stack.append(vertex)


if __name__=="__main__":
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

    print(f"Topological ordering: {DG.topological_sort()}")