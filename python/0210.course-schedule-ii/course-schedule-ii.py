class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjacency = [[] for _ in range(numCourses)]
        indegress = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegress[cur] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if not indegress[i]:
                queue.append(i)
        res = []
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            res.append(pre)
            for cur in adjacency[pre]:
                indegress[cur] -= 1
                if not indegress[cur]:
                    queue.append(cur)

        if not numCourses:
            return res
        else:
            return []

