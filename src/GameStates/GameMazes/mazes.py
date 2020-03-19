def open_maze(maze_number):
    maze_file = "maze_" + str(maze_number)

    with open(maze_file, r) as opened_file:
        raw_maze = opened_file.read()

    return _convert_maze(raw_maze)

def _convert_maze(raw_maze_string):
    raw_maze_string = raw_maze_string.splitlines()
    map_list = []
    temp_map_list = []
    # The 24 is for the resolution/block_width
    for row in raw_maze_string:
        for column in row:
            temp_map_list.append(column)

        map_list.append(temp_map_list)
        temp_map_list = []

    return map_list
