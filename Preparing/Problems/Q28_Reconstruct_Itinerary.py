class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        for dep, des in tickets:
            if dep not in graph:
                graph[dep] = [des]
            else:
                graph[dep].append(des)
        for dep in graph.keys():
            graph[dep].sort(reverse=True)
        
        res = []
        stack =["JFK"]
        
        while len(stack) >0:
            ele = stack[-1]
            if ele in graph and len(graph[ele]) > 0:
                stack.append(graph[ele].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
