import sys

def find_paths(maze, x, y, should_trace_all_paths = False):
    found_paths = set()
    def solve_maze(maze, row = 0, col = 0, current_path = '', should_trace_all_paths = False):
   
        if col < 0 or row < 0 or col >= len(maze[0]) or row >= len(maze):
            #We are out of the maze.
            return

        #Here we check if we have reached the exit.
        if maze[row][col] == 'e':
            found_paths.add(current_path)

        if maze[row][col] == ' ':
            #Here we mark the cell as visited.
            maze[row][col] = 's'

            solve_maze(maze, row, col-1, current_path + 'L', should_trace_all_paths)
            solve_maze(maze, row-1, col, current_path + 'U', should_trace_all_paths)
            solve_maze(maze, row, col+1, current_path + 'R', should_trace_all_paths)
            solve_maze(maze, row+1, col, current_path + 'D', should_trace_all_paths)


            if should_trace_all_paths:
                #After all the recursion calls have passed, we mark the cell back as unvisited.
                maze[row][col] = ' '
    maze_copy = [row[:] for row in maze]
    solve_maze(maze_copy, x, y, should_trace_all_paths=should_trace_all_paths)
    return found_paths

def find_shortest_path(maze, x, y):

    all_paths = find_paths(maze, x, y, should_trace_all_paths=True)
    return min(all_paths, key=len)




def main():
    #Here we have a very generic maze.
    maze = []
    maze.append([' ', ' ', ' ', '*', ' ', ' ', ' '])
    maze.append(['*', '*', ' ', '*', ' ', '*', ' '])
    maze.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
    maze.append([' ', '*', '*', '*', '*', '*', ' '])
    maze.append([' ', ' ', ' ', ' ', ' ', ' ', 'e'])

    #Here we have a maze without walls.
    maze_without_walls = []
    maze_without_walls.append([' ',' ',' '])
    maze_without_walls.append([' ',' ',' '])
    maze_without_walls.append([' ',' ','e'])

    #Here we have a maze that has a blocked exit.
    maze_with_blocked_exit = []
    maze_with_blocked_exit.append([' ', ' ', ' ', '*'])
    maze_with_blocked_exit.append([' ', '*', ' ', ' '])
    maze_with_blocked_exit.append([' ', '*', ' ', '*'])
    maze_with_blocked_exit.append([' ', ' ', '*', 'e'])

    #And here we have a big maze.
    big_maze = []
    big_maze.append([' ','*',' ',' ',' ',' ',' ',' ','*',' ',' ','*','*',' ','*'])
    big_maze.append([' ','*',' ','*','*','*','*',' ','*',' ',' ',' ',' ',' ','*'])
    big_maze.append([' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'])
    big_maze.append([' ',' ','*',' ',' ','*',' ',' ','*','*','*','*','*',' ','*'])
    big_maze.append([' ',' ','*',' ',' ','*',' ',' ','*',' ',' ',' ',' ',' ','*'])
    big_maze.append([' ',' ','*',' ',' ','*',' ',' ','*',' ',' ',' ',' ',' ','*'])
    big_maze.append([' ','*','*','*',' ','*',' ',' ','*',' ',' ','*','*','*','*'])
    big_maze.append([' ','*','*','*','*','*',' ',' ','*',' ',' ',' ',' ',' ',' '])
    big_maze.append([' ',' ',' ',' ',' ','*',' ',' ','*',' ',' ',' ',' ',' ','e'])

    w, h = map(int, input('Enter the coordinates of the player: ').split(' '))
    if maze[w][h] == '*':
        raise ValueError('The given coordinates are in a wall.')

    found_paths = find_paths(maze, w, h, True)
    print('All possible paths in the first maze: ')
    for path in found_paths:
        print('--' + path)

    shortest_path = find_shortest_path(maze, w, h)
    print('\nThe shortest path is: ' + shortest_path)

    found_paths = find_paths(maze_without_walls, w, h, True)
    print('\nAll paths for the maze without walls: ')
    for path in found_paths:
        print('--' + path)

    found_paths = find_paths(maze_with_blocked_exit, w, h, True)
    print('\nAll paths for the maze with a blocked exit (there shouldn\'t be any, since there is no way to reach the exit): ')
    for path in found_paths:
        print('--' + path)

    try:
        print('\nWe don\'t search for all paths, because the program freezes.')
        found_paths = find_paths(big_maze, w, h)
        for path in found_paths:
            print('--' + path)
    except RuntimeError:
        print("The program went too far into recursion.")





if __name__ == "__main__":
    sys.exit(int(main() or 0))