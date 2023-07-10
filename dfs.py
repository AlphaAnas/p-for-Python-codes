Nodes=['A','B','C','D', 'E','F','G']
di={}
edges=[('A','B',5),('B','C',6),('C','G',2),('G','F',10),('F','E',9),('A','E',6),('A','D',3),('C','D',10),('D','F',8)]

def addNodes(di, nodes):
    for ele in nodes:
        if ele not in di.keys():
            di[ele]=[]
        else:
            continue
    return di
def addEdges(di, edges,directed):

    for ele in edges:
        source=ele[0]
        goal=ele[1]
        weight=ele[2]
        tupl=(goal, weight)
        if source in di.keys():
            di[source].append(tupl)
        else:
            di[source]=[tupl]
    if not directed:
        for ele in edges:
            source=ele[1]
            goal=ele[0]
            weight=ele[2]
            tupl=(goal, weight)
            if source in di.keys():
                di[source].append(tupl)
            else:
                di[source]=tupl


    for i in di.values():
        i=i.sort()
   

    return di
print(addNodes(di,Nodes),'nodes added')
print(addEdges(di,edges,False),'edges added')

def dfs(di,source, visited):
    if source not in visited:
        visited.append(source)
        neighbour=di[source]
        for n in neighbour:
            ele=n[0]
            dfs(di, ele, visited)
    return visited
    
print(dfs(di, 'A',[]))
            