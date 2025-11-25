class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(node):
            queue=deque()
            queue.append(node)
            while queue:
                node=queue.popleft()
                for j in range(n):
                    if j==node:continue
                    if isConnected[node][j] and not visited[j]:
                        queue.append(j)
                        visited[j]=1
            return
        n=len(isConnected)
        count=0
        visited=[0]*n
        for node in range(n):
            if not visited[node]:
                bfs(node)
                count+=1
        return count

        