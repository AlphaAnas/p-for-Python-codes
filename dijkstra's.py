import heapq
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
            

def dijkstra(di,source):
    pq=[]
    preele=None
    cost={}# this 'll be returned in teh end
    heapq.heapify(pq)
    for i in di.keys():
        cost[i]=[9999999,preele]
    cost[source]=[0,None]
    heapq.heappush(pq, (cost[source][0],source)) # the source and its cost (in a tuple)
    while pq:
        tupl=heapq.heappop(pq)
        print(tupl)
        eleCost=tupl[0]
        eleLabel=tupl[1]
        for children in di[eleLabel]:
            weight=children[1]
            label=children[0]
            if weight + eleCost < cost[label][0]:
                cost[label][0]=weight + eleCost
                preele=eleLabel
                cost[label][1]=preele
                heapq.heappush(pq,(cost[label][0],label))

    return cost
cost=(dijkstra(di,'A'))
def dijkstras(di, source):
    pq=[]
    heapq.heapify(pq)
    cost={}
    preele=None
    
    for i in di.keys():
        cost[i]=[99999999, preele]
    cost[source]=[0,None]
    heapq.heappush(pq, (cost[source][0],source))
    while pq:
        ele=heapq.heappop(pq)
        label=ele[1]
        weight=[0]
        for e in di[label]:
            eleLabel=e[0]
            elecost=e[1]
            if elecost+weight<cost[eleLabel][0]:
                cost[eleLabel][0]= elecost+weight
                preele=label
                cost[label][1]=preele
                heapq.heappush(pq,(cost[label][0],label))


print(cost)

current='G'
outlst=[]
while current!='A':

  tupl=(cost[current][1],current)
  outlst.append(tupl)
  current=cost[current][1]
  
outlst.reverse()
print(outlst,'ans')
