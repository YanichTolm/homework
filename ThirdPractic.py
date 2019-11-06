import re
from datetime import datetime

start_time = datetime.now()
def  makematrix(V, G):
    matrix = []
    for i in range(0, V):
        matrix.append([])
        for j in range(0, V):
            matrix[i].append(0)
    for i in range(0, len(G)):
        matrix[G[i][0]][G[i][1]] = G[i][2]
        matrix[G[i][1]][G[i][0]] = G[i][2]
    return matrix

def primalg(V, G):
    matrix = makematrix(V, G)
    vertex = 0
    MST = []
    edges = []
    visited = []
    minEdge = [None, None, float('inf')]
    while len(MST) != V - 1:
        visited.append(vertex)
        for r in range(0, V):
            if matrix[vertex][r] != 0:
                edges.append([vertex, r, matrix[vertex][r]])
        for e in range(0, len(edges)):
            if edges[e][2] < minEdge[2] and edges[e][1] not in visited:
                minEdge = edges[e]
        edges.remove(minEdge)
        MST.append(minEdge)
        vertex = minEdge[1]
        minEdge = [None, None, float('inf')]
    return MST


# a, b, c, d, e, f, g, h, k,  m, n, p, q
# 7, 2, 1, 4, 8, 8, 6, 3, 4, 10, 7, 4, 4

#the first two numbers are vertex numbers, the count starts at 0
#the third number is the weight of the edge between these vertices
graph = [
    [0, 1, 2],
    [0, 3, 1],
    [0, 4, 7],
    [1, 2, 4],
    [1, 5, 3],
    [2, 5, 10],
    [2, 7, 7],
    [3, 4, 4],
    [3, 6, 8],
    [4, 6, 8],
    [4, 7, 6],
    [5, 7, 4],
    [6, 7, 4]
]
print("(Первые два числа - номера вершин, счет начинается с 0."
              " \n Третье число - вес ребра между этими вершинами.)")
print("\n Алгоритм Прима: ")
print("Значение рёбер, которые образуют остовое дерево:")
print( primalg(8, graph))

end_time = datetime.now()
print('Продолжительность работы алгоритма: {}'.format(end_time - start_time))
# ~~~0:00:00.000998


start_time = datetime.now()
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xRoot = self.find(parent, x)
        yRoot = self.find(parent, y)
        if rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        elif rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        else:
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def kruskalalg(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        print("\n Алгоритм Крускала: ")
        print("Значение рёбер, которые образуют остовое дерево:")
        for u, v, weight in result:
            print("[%d, %d, %d], " % (u,v,weight), end="")


g = Graph(8)
g.addEdge(0, 1, 2)
g.addEdge(0, 3, 1)
g.addEdge(0, 4, 7)
g.addEdge(1, 2, 4)
g.addEdge(1, 5, 3)
g.addEdge(2, 5, 10)
g.addEdge(2, 7, 7)
g.addEdge(3, 4, 4)
g.addEdge(3, 6, 8)
g.addEdge(4, 6, 8)
g.addEdge(4, 7, 6)
g.addEdge(5, 7, 4)
g.addEdge(6, 7, 4)

g.kruskalalg()

end_time = datetime.now()
print('\nПродолжительность работы алгоритма: {}'.format(end_time - start_time))
# ~~~ 0:00:00.000996
