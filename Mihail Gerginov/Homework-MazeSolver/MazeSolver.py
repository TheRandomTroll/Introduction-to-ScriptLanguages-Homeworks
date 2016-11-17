import sys

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


def find_shortest_path(maze, x, y):
    solve_maze(maze, x, y, should_trace_all_paths=True)
    return min(found_paths, key=len)




def main():
    maze = []
    maze.append([' ', ' ', ' ', '*', ' ', ' ', ' '])
    maze.append(['*', '*', ' ', '*', ' ', '*', ' '])
    maze.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
    maze.append([' ', '*', '*', '*', '*', '*', ' '])
    maze.append([' ', ' ', ' ', ' ', ' ', ' ', 'e'])


    w, h = map(int, input('Enter the coordinates of the player: ').split(' '))
    if maze[w][h] == '*':
        raise ValueError('The given coordinates are in a wall.')

    solve_maze(maze, w, h, should_trace_all_paths=True)
    print('All possible paths: ')
    for path in found_paths:
        print('--' + path)

    shortest_path = find_shortest_path(maze, w, h)
    print('The shortest path is: ' + shortest_path)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
