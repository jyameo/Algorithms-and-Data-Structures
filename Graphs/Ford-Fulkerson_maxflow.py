import math
from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self.rows = len(graph)

    def bfs(self, s,t,parent):
        visited = [False]*self.rows
        q = [s]
        visited[s] = True

        while q:
            u = q.pop(0)

            for v, val in enumerate(self.graph[u]):
                if visited[v] == False and val > 0:
                    q.append(v)
                    visited[v] = True
                    parent[v] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.rows)
        max_flow = 0

        # While a path exist from source to sink and min capacity > 0
        while self.bfs(source, sink, parent):
            # Find min path flow
            min_path_flow = math.inf
            v = sink

            while v != source:
                u = parent[v]
                min_path_flow = min(min_path_flow, self.graph[u][v])
                v = u
            

            max_flow += min_path_flow
            v = sink
            # Update residual capacity
            while v != source:
                u = parent[v]
                self.graph[u][v] -= min_path_flow
                self.graph[v][u] += min_path_flow
                v = u
        return max_flow


graph = [[0, 16, 13, 0, 0, 0], 
        [0, 0, 10, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 4], 
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source, sink = 0,len(graph)-1

print("Max Flow :", g.ford_fulkerson(source, sink))
