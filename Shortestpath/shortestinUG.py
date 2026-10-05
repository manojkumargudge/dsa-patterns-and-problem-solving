'''Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, where edges[i] = [u, v] denotes an undirected edge between vertex u and vertex v, given two vertices src and dest, find the length of the shortest path from src to dest. If there is no path between src and dest, return -1.

Note: All edges have a unit weight of 1.'''

from collections import deque



class Solution:
    def shortestpath(self,adj,src):
        n = len(adj)
        distance = [-1 for _ in range(n)]
        queue = deque()
        queue.append([src,0])
        distance[src]=0
        while len(queue)!=0:
            node,dist_travel = queue.popleft()
            for adjNode in adj[node]:
                distance[adjNode] = dist_travel +1
                queue.append[adjNode,dist_travel+1]

        return distance
    
        