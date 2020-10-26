from collections import defaultdict
from queue import Queue

import networkx as nx


class BfsTraverser:
  # Constructor
  def __init__(self):
    #self.visited = []
    #self.end_search = False
    self.visited={}
    self.steps={}
    self.parent={}
    self.output=[]
    self.queue=Queue()
    self.path=[]
  def BFS(self,graph, start_node, goal_node):
    print(self.queue)
    for node in graph.nodes.keys():
      self.visited[node]=False
      self.parent[node]=None
      self.steps[node]=-1



    s=start_node
    self.visited[s]=True
    self.steps[s]=0
    self.queue.put(s)


    #set of visited nodes
    #self.visited.append(start_node)
    while not self.queue.empty():


      # Dequeue a vertex from
      u = self.queue.get()
      self.output.append(u)

      for v in list(graph[u]):
        if not self.visited[v]:
          self.visited[v]=True
          self.parent[v]=u
          self.steps[v]=self.steps[u]+1
          self.queue.put(v)

    print(self.steps)
    p=goal_node
    while p is not None:
      self.path.append(p)
      p=self.parent[p]
    self.path.reverse()


