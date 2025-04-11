from collections import deque

def solve(dungeon, start):
    R, C = len(dungeon), len(dungeon[0])
    sr, sc = start
    rq, cq = deque(), deque()
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    reached_end = False
    visited = [[False] * C for _ in range(R)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    def explore_neighbours(r, c):
        nonlocal nodes_in_next_layer
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if rr < 0 or cc < 0 or rr >= R or cc >= C:
                continue
            if visited[rr][cc] or dungeon[rr][cc] == '#':
                continue
            rq.append(rr)
            cq.append(cc)
            visited[rr][cc] = True
            nodes_in_next_layer += 1

    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True

    while rq:
        r, c = rq.popleft(), cq.popleft()
        if dungeon[r][c] == 'E':
            reached_end = True
            break
        explore_neighbours(r, c)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    return move_count if reached_end else -1

dungeon = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.'],
    ['#', '.', '#', 'E', '.', '#', '.']
]

start = (0, 0)

steps_to_escape = solve(dungeon, start)
print(f"{steps_to_escape} Քայլ պահանջվեց դուրս գալու համար")