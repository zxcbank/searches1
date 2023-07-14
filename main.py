'''
adj - списки смежности
ms - матрицы смежности с ценами ребер
'''

def BFS(start, end, graph, v):
    '''
    :param start: старт
    :param end: конец
    :param graph: граф
    :param v: колво вершин
    :return: Есть ли Вершина в графе
    '''
    visited = [False] * v
    visited[start] = True
    queue = [start]

    while (len(queue) > 0):
        v0 = queue.pop(0)
        if v0 == end:
            return True
        else:
            for u in graph[v0]:
                if not visited[u]:
                    visited[u] = True
                    queue.append(u)
    return False


def DFS(start, end, graph, v):
    '''
        :param start: старт
        :param end: конец
        :param graph: граф
        :param v: колво вершин
        :return: Есть ли Вершина в графе, путь
        '''
    visited = [False] * v
    stack = [start]
    visited[start] = True
    way = []

    while len(stack) > 0:
        v0 = stack[0]
        way.append(v0)
        if v0 == end:
            return True, way
        else:
            childs = []
            for i in graph[v0]:
                if not visited[i]:
                    visited[i] = True
                    childs.append(i)
            if len(childs) == 0:
                way.remove(stack.pop(0))
            else:
                stack = childs + stack
    return False

def adj_to_1_dir_graph(adj, v):
    ms = [[0 for m in range(v)] for k in range(v)]

    for i in range(v):
        tmp = len(adj[i])
        for j in range(tmp):
            if i < adj[i][j]:
                ms[i][adj[i][j]] = 1
    return ms


# bfs dfs example graph1
adj1 = [[1, 2], [0, 4, 5, 6], [0, 3, 7], [2, 8], [1], [1], [1, 7, 9], [2, 6, 8, 9], [3, 7, 10], [6, 7, 12], [8, 11],
     [10, 12], [9, 11]]
v1 = 13
# bfs dfs example
# dijkstra example graph 2
ms2 = [[0, 80, 0, 0, 0, 50, 0, 0], [0, 0, 10, 0, 0, 0, 0, 0], [0, 0, 0, 20, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 4, 0, 0, 0, 0, 60], [0, 0, 0, 0, 30, 0, 100, 0], [0, 0, 0, 0, 0, 0, 0, 60], [0, 0, 0, 90, 0, 0, 0, 0]]

adj2 = [[1, 5], [2], [3], [], [2, 7], [4, 6], [7], [3]]
v2 = 8


# dijkstra example graph

def ms_to_adj(ms, v):
    adj = [[] for i in range(v)]
    for i in range(v):
        for j in range(v):
            if ms[i][j] != 0:
                adj[i].append(j)
    return adj


def dijkstra(start, finish, ms, adj, v):
    '''
    не работает для графиках с тупиками
    '''
    tmp_ms = [[ms[j][i] for i in range(v)] for j in range(v)]
    dist = [99999999] * v
    completed = [False] * v
    completed[start] = True
    dist[start] = 0
    queue = [start]
    last = [-1] * v
    last[0] = 0

    while not all(completed):
        v0 = queue.pop(0)  # убираем из очереди вершину, тк мы ее либо продолжим, либо нет
        print(v0, dist)
        flag = True
        # этот фор нужен для того, чтобы проверить, что все входящие ребра учтены, иначе мы просто скипаем эту вершину
        for j in range(v):
            if tmp_ms[j][v0] != 0:  # если есть хоть одно входящее в эту вершину ребро, то дальше по нему не идем
                flag = False
        if flag:
            completed[v0] = flag
            for i in adj[v0]:  # перебираем все исходящие вершины
                new_dist = dist[v0] + ms[v0][i]
                tmp_ms[v0][i] = 0  # исключаем ребро и списка ребер, типо оно уже пройдено
                if dist[i] > new_dist:
                    dist[i] = new_dist
                    last[i] = v0
                queue.append(i)

    x = -1
    way = [v-1]
    while x != 0:
        x = last[x]
        way.append(x)
    return dist[finish], dist, way[::-1]

print(dijkstra(0, 3, ms2, adj2, v2))
