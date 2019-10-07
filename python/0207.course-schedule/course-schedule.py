class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = [[] for _ in range(numCourses)]
        indegress = [0 for _ in range(numCourses)]
        queue = collections.deque()
        # Get adjacency from information
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegress[cur] += 1
        # Get all 0 indgree nodes
        for i in range(numCourses):
            if not indegress[i]:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                # reduce one indgress
                indegress[cur] -= 1
                if not indegress[cur]:
                    queue.append(cur)
        return not numCourses
