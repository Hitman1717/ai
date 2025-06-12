def dfs(g : dict , root):
    n = len(g)
    visited = [False for i in range(n)]
    visited[root-1] = True
    stack = list()
    stack.append(root)
    completed = list()
    while(len(stack) != 0 ):
        cur = stack.pop()
        completed.append(cur)
        visited[cur-1] = True
        for node in graph[cur] :
            if (not visited[node-1]):
                stack.append(node)
    print("DFS :-\t",completed)

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


dfs(graph,1)