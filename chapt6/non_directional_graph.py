

class Graph:
    def __init__(self, num_nodes):
        self.nodes = num_nodes
        self.matrix = self.create_matrix(self.nodes)

        
    def create_matrix(self, num_nodes):
        return [[0] * num_nodes for _ in range(num_nodes)]

    def show_matrix(self):
        print('===============')
        for i in range(self.nodes):
            for j in range(self.nodes):
                pass
                print(f'{self.matrix[i][j]:>3}', end='')
            print('')
        print('===============')

    def add_edge(self, start, end, value = 1):
        self.matrix[start][end] = self.matrix[end][start] = value
    
    def remove_edge(self, start, end):
        self.matrix[start][end] = self.matrix[end][start] = 0

    def get_neighbours(self, node):
        neighbors = []
        for i in range(self.nodes):
            if self.matrix[node][i] != 0:
                neighbors.append(i)
        return neighbors

    def bf_search(self, start, end):
        verified = set()
        parents = {start: None}
        queue = [start]
        
        while len(queue) != 0:
            node = queue.pop(0)
        
            if node not in verified:
                verified.add(node)

                if node == end:
                    return True, self.backtrace(start, end, parents)

                for neighbour in self.get_neighbours(node):
                    queue.append(neighbour)
                    if neighbour not in parents:
                        parents[neighbour] = node
        return False
    
    def backtrace(self, start, end, parents):
        path = [end]

        while start not in path:
            actual = parents[end]
            path.append(actual)

            end = actual
        path.reverse()

        return path


        

def main():
    graph = Graph(4)
    graph.show_matrix()

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.show_matrix()

    a,b = graph.bf_search(0, 3)

    print(a)
    print(b)


if __name__ == '__main__':
    main()



