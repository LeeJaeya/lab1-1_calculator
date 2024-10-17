#DFS 연습입니다.
#수업에서는 재귀함수가 쓰였으므로 이번에는 스택을 사용해보겠습니다.

adj_list = [[4,3,1],[5,3,2,0],[7,5,1],[5,4,1,0],[6,5,3,0],[7,6,4,3,2,1],[7,5,4],[6,5,2]]
visited = [False for _ in adj_list]
route = []

def dfs(list, v):
    stack = [v]

    while stack:
        w = stack.pop()
        #if문을 수행하려면 if True가 되야하므로
        if not visited[w]:
            visited[w] = True
            route.append(w)
            stack.extend(reversed(list[w]))

for i in range(len(adj_list)):
    if not visited[i]:
        dfs(adj_list, i)

print(f"방문순서: {route}")