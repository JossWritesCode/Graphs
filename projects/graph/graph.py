"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()  # set of edges

    def add_edge(self, v1, v2):
        """add edge from v1 to v2."""
        """
        Add a directed edge to the graph.
        """
        # if they're both in the graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        Breadth-First Traversal
        Add starting node to a queue
        While queue isn't empty:
            Dequeue the first vert
            If that vert isn't visited:
                Mark as visited
                Add all its unvisited neighbors to the queue

        """

        q = Queue()
        q.enqueue(starting_vertex_id)

        # Keep track of visited nodes
        visited = set()
        # Repeat until queue is empty
        while q.size() > 0:
            # Dequeue first vert
            v = q.dequeue()
            # If it's not visited:
            if v not in visited:
                print(v)
                # mark visited
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex_id):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        Depth-First Traversal
        Add starting node to a stack
        While stack isn't empty:
            Pop the first vert
            If that vert isn't visited:
                Mark as visited
                Push all its unvisited neighbors to the stack
        """

        s = Stack()
        s.push(starting_vertex_id)

        # Keep track of visited nodes
        visited = set()
        # Repeat until queue is empty
        while s.size() > 0:
            # Dequeue first vert
            v = s.pop()
            # If it's not visited:
            if v not in visited:
                print(v)
                # mark visited
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def helper_function(self, starting_vertex, visited):
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            for next_vert in self.get_neighbors(starting_vertex):
                self.helper_function(next_vert, visited)
        else:
            return

    def dft_recursive(self, starting_vertex):
        visited = set()
        self.helper_function(starting_vertex, visited)

    def bfs(self, starting_vertex_id, destination_vertex_id):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue(starting_vertex_id)

        # Keep track of visited nodes
        visited = set()

        if starting_vertex_id is destination_vertex_id:
            return starting_vertex_id

        # Repeat until queue is empty
        while q.size() > 0:
            # Dequeue first vert
            path = [q.dequeue()]
            node = path[-1]
            # If it's not visited:
            if node not in visited:
                neighbors = self.get_neighbors(node)

                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                   # return path if neighbour is goal
                    if neighbor is destination_vertex_id:
                        return new_path
                # mark visited
                visited.add(node)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
