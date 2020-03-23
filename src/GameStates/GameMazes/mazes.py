def load_map(map_number):
    # TODO: Use os to get path names that will work for Windows, Mac, and Linux instead
    # of just Windows.
    map_file = "src\GameStates\GameMazes\maze_" + str(map_number)

    with open(map_file, "r") as opened_file:
        raw_map = opened_file.read()

    return _convert_map(raw_map)

# Converts the string into a list.
def _convert_map(raw_map_string):
    raw_map_string = raw_map_string.splitlines()
    map_list = []
    temp_map_list = []

    for row in raw_maze_string:
        for character in row:
            temp_map_list.append(character)

        map_list.append(temp_map_list)
        temp_map_list = []

    return map_list
