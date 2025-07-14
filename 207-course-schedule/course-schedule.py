class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        inDegree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            inDegree[dest] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        count = 0

        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in graph[current]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses

