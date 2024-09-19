from collections import deque, defaultdict

def catMouseGame(graph):
    n = len(graph)
    dp = defaultdict(lambda: -1)  

    def bfs():
        queue = deque()
        for i in range(1, n):
            queue.append((0, i, 0))  
            dp[(0, i, 0)] = 0
            queue.append((i, i, 1)) 
            dp[(i, i, 1)] = 1

        while queue:
            mouse, cat, turn = queue.popleft()
            current_result = dp[(mouse, cat, turn)]
            next_turn = 1 - turn
            if turn == 0:  
                for next_mouse in graph[mouse]:
                    if dp[(next_mouse, cat, next_turn)] == -1:
                        if current_result == 0:  
                            dp[(next_mouse, cat, next_turn)] = 0
                            queue.append((next_mouse, cat, next_turn))
                        else:
                            if all(dp[(next_mouse, cat, next_turn)] == 1 for next_mouse in graph[next_mouse]):
                                dp[(next_mouse, cat, next_turn)] = 2
                                queue.append((next_mouse, cat, next_turn))
            else:  
                for next_cat in graph[cat]:
                    if next_cat != 0:  
                        if dp[(mouse, next_cat, next_turn)] == -1:
                            if current_result == 1:  
                                dp[(mouse, next_cat, next_turn)] = 1
                                queue.append((mouse, next_cat, next_turn))
                            else:
                                if all(dp[(mouse, next_cat, next_turn)] == 0 for next_cat in graph[next_cat] if next_cat != 0):
                                    dp[(mouse, next_cat, next_turn)] = 2
                                    queue.append((mouse, next_cat, next_turn))
    
    bfs()
    
    return dp[(1, 2, 0)]

# Example usage
print(catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]))  
