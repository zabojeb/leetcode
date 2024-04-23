class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj_list = defaultdict(list)
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)

        leaves = [node for node in range(n) if len(adj_list[node]) == 1]

        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)

            new_leaves = []

            for leaf in leaves:
                neighbor = adj_list[leaf][0]
                adj_list[neighbor].remove(leaf)

                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
