class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodes = [set() for i in range(n)]
        for edge in edges:
            nodes[edge[0]].add(edge[1])
            nodes[edge[1]].add(edge[0])
        leaves = []
        remain = set(range(n))
        for i in range(len(nodes)):
            if len(nodes[i]) == 1:
                leaves.append(i)
        while leaves:
            if len(remain) <= 2: break
            nextLeaves = []
            for node in leaves:
                remain.remove(node)
                vex = nodes[node].pop()
                nodes[vex].remove(node)
                if len(nodes[vex]) == 1:
                    nextLeaves.append(vex)
            leaves = nextLeaves
        return list(remain)
if __name__ == "__main__":
    s = Solution()
    n = 4
    edges = [[1,0], [1,2], [1,3]]
    res = s.findMinHeightTrees(n, edges)
    print(res)
