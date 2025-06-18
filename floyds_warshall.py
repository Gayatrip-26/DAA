v=3
INF=float('INF')
graph=[
    [0,4,15],
    [8,0,2],
    [3,INF,0],
]

for k in range(len(graph)):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                  graph[i][j] = graph[i][k] + graph[k][j]

r=1

for row in range (len(graph)):
    c=1
    for col in range(len(graph)):
        print(f"The shortest distance from {r}----->{c} is ={graph[row][col]} ")

        c+=1
    r+=1
