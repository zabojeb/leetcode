class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, graph, vis, destination):
            if node == destination:
                return True

            vis[node] = True

            for neighbor in graph[node]:
                if not vis[neighbor]:
                    if dfs(neighbor, graph, vis, destination):
                        return True
                        
            return False

        graph = defaultdict(list)

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        vis = [False]*n

        return dfs(source, graph, vis, destination)
