def open_maze(maze_number):
    maze_file = "maze_" + str(maze_number)

    with open(maze_file, r) as opened_file:
        raw_maze = opened_file.read()

    return _convert_maze(raw_maze)

