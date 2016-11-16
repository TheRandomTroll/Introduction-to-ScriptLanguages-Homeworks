import sys

paths_found = []
def find_all_paths(maze, row = 0, col = 0, current_path = ""):
    if col < 0 or row < 0 or col >= len(maze[0]) or row >= len(maze):
        #We are out of the maze.
        return

    #Here we check if we have reached the exit.
    if maze[row][col] == 'e':
        paths_found.append(current_path)

    if maze[row][col] == ' ':
        #Here we mark the cell as visited.
        maze[row][col] = 's'

        find_all_paths(maze, row, col-1, current_path + 'L')
        find_all_paths(maze, row-1, col, current_path + 'U')
        find_all_paths(maze, row, col+1, current_path + 'R')
        find_all_paths(maze, row+1, col, current_path + 'D')


        maze[row][col] = ' '

def find_at_least_one_path(maze, row = 0, col = 0, current_path = ""):
    if col < 0 or row < 0 or col >= len(maze[0]) or row >= len(maze):
        #We are out of the maze.
        return

    #Here we check if we have reached the exit.
    if maze[row][col] == 'e':
        paths_found.append(current_path)

    if maze[row][col] == ' ':
        #Here we mark the cell as visited.
        maze[row][col] = 's'

        find_at_least_one_path(maze, row, col-1, current_path + 'L')
        find_at_least_one_path(maze, row-1, col, current_path + 'U')
        find_at_least_one_path(maze, row, col+1, current_path + 'R')
        find_at_least_one_path(maze, row+1, col, current_path + 'D')


def find_shortest_path(maze):
    find_all_paths(maze)
    return min(paths_found, key=len)



def main():
    maze = []
    maze.append([' ', ' ', ' ', '*', ' ', ' ', ' '])
    maze.append(['*', '*', ' ', '*', ' ', '*', ' '])
    maze.append([' ', ' ', ' ', ' ', ' ', ' ', ' '])
    maze.append([' ', '*', '*', '*', '*', '*', ' '])
    maze.append([' ', ' ', ' ', ' ', ' ', ' ', 'e'])
    w, h = map(int, input("Enter the coordinates of the player: ").split(' '))
    if maze[w][h] == '*':
        raise ValueError("The given coordinates are in a wall.")
    find_at_least_one_path(maze, w, h, "")
    for path in paths_found:
        print(path)


if __name__ == "__main__":
    sys.exit(int(main() or 0))
