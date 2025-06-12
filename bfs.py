def bfs(g : dict , root):
    n = len(g)
    visited = [False for i in range(n)]
    visited[root-1] = True
    queue = list()
    queue.append(root)
    completed = list()
    while(len(queue) != 0 ):
        cur = queue.pop(0)
        completed.append(cur)
        for node in graph[cur] :
            if (not visited[node-1]):
                visited[node-1] = True
                queue.append(node)
    print("BFS :-\t",completed)

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [1],      
    5: [6],
    6: [3, 8],   
    7: [8],
    8: [9],
    9: [10],
    10: [7]    
}


bfs(graph,1)