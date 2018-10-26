class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        dic = {}
        for line in tickets:
            if line[0] not in dic:
                dic[line[0]] = [line[1]]
            else:
                dic[line[0]].append(line[1])
        for x in dic:
            dic[x].sort()
        res = [0 for x in range(1 + len(tickets))]
        res[0] = "JFK"
        def find(dic, res, start, port):
            if start == len(res): return True
            for i in range(len(dic[port])):
                if dic[port][i] != "#":
                    res[start] = dic[port][i]
                    dic[port][i] = "#"
                    nextRes = find(dic, res, 1 + start, res[start])
                    if nextRes: return True
                    dic[port][i] = res[start]
            return False
        find(dic, res, 1, "JFK")
        return res

if __name__ == "__main__":
    s = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    print(s.findItinerary(tickets))
