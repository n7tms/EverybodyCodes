# 15a - trying a different algorithm
# https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

# How do I create a graph like the one in the link?
# or How do I modify the code below to use an adjacency list?

# This solution will work -- if I get desperate!
# https://topaz.github.io/paste/#XQAAAQCMDgAAAAAAAAARiAcH4cNcktpwLwcwtIOgpuFZqTzxZgRurfBoL6pYx4GY93Y0ok5Atwf3VpZxrrpdFHTE8QqSjpN9g46IES8e/S1MmP/gIb1bTFYSmc51HogGmZKgTiqlpqU+v3c+gSTr+loSqfbla4T3dEYfNGXtZy/250rP+bMFBkVHtC4IUgRe8MoltJLy+FMHXtMwlXwiE73H8rdGvWef6RSwOqlpcw0ELyPapyCqDuJb0hvab9ZytuP7vZzICWQB1ogH//+Sh0xusAdbF8Lm2SNEyUwDMm+49EFT6h+ajYHOmCWyPqPvm4qoL7jZ3jM/Mypu89fGNoysXqUSegYFXtaFFhXUIYzzTRO+Hpj2UennClJnybhzxWr3bPpeg+O6PtCKZLGXbOrS0BsTBTG7QBtIk3NivgYSLVu4STWeJzS6oO2+qfQH3jN/yQVWpT5U1xFNEEr/RUlqUK0y7X3bC3FqC41NTbeaecHTvt9ROIlTK9PA4vQ08aCjr0gvDgecHHoAunmK7jfsXsEm+TK1amMYhDljOax/DcER5HsHSvZuqXlZ/r2XVarMDWWe7NxcVnyHflIoUY2QgeZqafTM5A1HP0A/AsFdnFHjMuR0HXirWp77MESzx1rzcthtlq0ii5vgcxKzrUWGzuIVfH/8dpLEsicqZiDrLZVE0AevKlr2qKzraVahDBp6f+d095+9fE5rgrs1AloEsbc5yjFyVFQhmOUn2teWRJLXA6IFbIYC3xIbNB6Pq3AbbvZoqwIe/1/CNZfnn0lESsAXs8J9K8bMsd8+fUqSe5K61lKuTPc4xK122sj4htBfN0NBAgN69PoMKZWyeUmk7TEOLsGTXcn6eAGZnBXSE2Hg9IxoDAKa97AWRz7pXVKrxctKshOTDZzjGttqP5qypaIP0wHWfBfj3/eeizBDQIAFA53wyZOon7j5+cBDguDPN+TENqDn1/MDXbKvcWJltxYPTiMMayrJuzsL1mNOUAVe3CLVJ3toZOsaBl3/SJI9DZAfchUFD1Uey2kOMehxmrkdkhfI9TSORIMTWaF8B1d/Dup8QIOhBVNmxDffjSP4omGwFLgQ46Yx+spYcQCsUOEOCOP25Uys7zywb0ll47NV8agIkHWfzPZO7AJj2lZ3tiZogoytBu+UxB6nh1wo9r2JXD2BgjwRvyO1Jo4rQntjLamHs+gKxdh2r9ZpkOTuD4j8SVsCaH+F6Qcgb4/f+WL4BizemwOuBqBpl25Ovz4h4trb+a7ajYp+5jTsj0yUzq6mBUx2h7nXGxr22sqwRfGvV+YgSPCcHTcEP3/dBejSEjYl5Wm0bmk3LsOnTqE72FxDsuJMg8TQd7+vJNzdipste1kxVAK2DlYzuQVlW8YUQHUgw0gA+keT+R3DZSZ8akjaeHUENYQzxmGDSW9SepfRX0Lqr12/B+BMCbVZFARXCFq8Ih6xCCE+1CaN5a343wy1FxQD3kTXx9Lvzgf1iD7Brqha7w607I3bdtPFk4ToJVQrwNOtzZJt4EAKRxupnAe+bTE5OZd5wNP2EeM7LSb3V8v52LaSPbvKasU39WUke61+k4voSj//rP8MMe5Ipl9UhbW+LDcLiQ4Kr4Y99cFaI0+oyiWHI8F4k6vpzJueM4u1sZunaMXJCve+aKxmMz474bmFTorgb7X9l4i1HMS+DRF/FrpsYNjBIE5cWoS2hs/DAAhDNkEXwjt3s5CoADtdbrrcQwSfEFKOPdAbIwEwB35XD+wJly6LhfWUvQzxidd1Kqueo2Bv8ipTDY4+9XSHlOSSjhz7KyYxoime5jWABfD4TSRY1Tl868E9I0Ubq+W1Nm4/Y4aQT1ecDTRFpJv0c413HVBzgDCRKlDMTTDI602SwiA/f8IpFg9edagyAOa0SrJV7/m8GoWLFHHLRwRyVHpS3sOu+67x7WBeFzC8kP6wr98iaGRHwhDQnbV0Xq3T/7WbSb0=



class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data


    def dijkstra(self, start_vertex_data):
            start_vertex = self.vertex_data.index(start_vertex_data)
            distances = [float('inf')] * self.size
            distances[start_vertex] = 0
            visited = [False] * self.size

            for _ in range(self.size):
                min_distance = float('inf')
                u = None
                for i in range(self.size):
                    if not visited[i] and distances[i] < min_distance:
                        min_distance = distances[i]
                        u = i

                if u is None:
                    break

                visited[u] = True

                for v in range(self.size):
                    if self.adj_matrix[u][v] != 0 and not visited[v]:
                        alt = distances[u] + self.adj_matrix[u][v]
                        if alt < distances[v]:
                            distances[v] = alt

            return distances