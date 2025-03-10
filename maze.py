import sparsemat as sp

def path(maze, en, ex):
    stack = [en]
    visited = {en}
    maze = sp.convertToSparseMatrix(maze)
    return explore(maze, visited, stack, ex)


def explore(maze, visited, stack, ex):

   #if stack got empty no path is possible
    if not stack:
        return None
    
    current = stack[-1]
    if current == ex:
        return stack
    
    i, j = current
    neighbors = sorted( [(i+1, j), (i-1, j), (i, j+1), (i, j-1)], key= lambda ne: abs(ne[0] - ex[0]) + abs(ne[1] - ex[1]) )

    for next in neighbors:
        x, y = next
        if 0 <= x < maze.row_count() and 0 <= y < maze.col_count() and maze.get_value(x, y) == 0 and next not in visited:
            visited.add(next)
            stack.append(next)
            path = explore(maze, visited, stack, ex)
            if path:
                return path
            #if path is none go back in previous location and try another direction
            stack.pop()
    #if did not reach the end and there is not any new availabe neighbour return none
    return None
        
maze = [
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 0, 0]
           ]


start = (0, 0)
end = (3, 3)
# Expected Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6)]



path1 = path(maze, start, end)
if path1:
    print("Path found:", path1)
else:
    print("No path exists")
