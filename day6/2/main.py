import re

def main():
    global data
    state = 0
    position = None
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
        for i in range(len(data)):
            player = re.search(r"[v<>^]", data[i])
            if player:
                position = (i, player.start())
                match player.group():
                    case "^":
                        state = 0
                    case ">":
                        state = 1
                    case "v":
                        state = 2
                    case "<":
                        state = 3
                break
    
    if position is None:
        print("No player character found in input")
        return
    
    print(position, state)

    positions = find_path(data, position, state)

    print(len(positions))

    distinct_positions = find_loops(data, positions, position, state)

    print(len(distinct_positions))


def calculate_new_position(current_position, current_state, data):
    new_position = None
    match current_state:
        case 0:
            new_position = (current_position[0] - 1, current_position[1])
        case 1:
            new_position = (current_position[0], current_position[1] + 1)
        case 2:
            new_position = (current_position[0] + 1, current_position[1])
        case 3:
            new_position = (current_position[0], current_position[1] - 1)

    if new_position[0] < 0 or new_position[0] >= len(data) or new_position[1] < 0 or new_position[1] >= len(data[0]):
        return None

    return new_position

def find_path(data, position, state):
    positions = {}
    current_position = position
    current_state = state

    while True:
        if not positions.get(current_position):
            positions[current_position] = [];
        if not current_state in positions[current_position]:
            positions[current_position].append(current_state)

        # Calculate new position based on current state
        new_position = calculate_new_position(current_position, current_state, data)
        if new_position is None:
            return positions

        target = get_position(data, new_position[0], new_position[1])

        match target:
            case "#":
                current_state = rotate_direction(current_state)
            case None:
                return positions
            case _:
                current_position = new_position

def rotate_direction(state):
    return (state + 1) % 4

def get_position(data, i, j):
    if i >= 0 and i < len(data) and j >= 0 and j < len(data[i]):
        return data[i][j]
    return None

def find_loops(data, positions, starting_position, starting_state):
    distinct_positions = {}
    for i in range(len(positions)):
        print("Testing ",i,"/",len(positions))
        position = list(positions.keys())[i]
        for state in positions[position]:
            new_position = calculate_new_position(position, state, data)
            if new_position is None:
                continue
        
            if data[new_position[0]][new_position[1]] == "#":
                continue
            if data[new_position[0]][new_position[1]] in ["<", ">", "^", "v"]:
                continue

            verbose = False
            print(new_position)
            test_result = test_loop(data, starting_position, starting_state, new_position, verbose)
            if test_result is not None:
                if not distinct_positions.get(test_result):
                    distinct_positions[test_result] = True

    return distinct_positions

def test_loop(data, starting_position, starting_state, test_position, verbose = False):
    positions = {}
    # Convert strings to lists of characters to make them mutabl
    data_copy = [list(row) for row in data]
    #data_copy[test_position[0]][test_position[1]] = "S"
    data_copy[test_position[0]][test_position[1]] = "O"

    current_position = starting_position
    current_state = starting_state
    while True:
        if(current_position in positions):
            if(current_state in positions[current_position]):
                return test_position

        # Calculate new position based on current state
        new_position = calculate_new_position(current_position, current_state, data_copy)
        if new_position is None:
            if(verbose):
                print("No loop found")
            return None

        target = get_position(data_copy, new_position[0], new_position[1])
        match target:
            case "#":
                current_state = rotate_direction(current_state)
            case "O":
                current_state = rotate_direction(current_state)
            case None:
                if(verbose):
                    print("No loop found")
                return None
            case _:
                data_copy[current_position[0]][current_position[1]] = "X"
                if(positions.get(current_position) is None):
                    positions[current_position] = []
                positions[current_position].append(current_state)
                current_position = new_position


if __name__ == "__main__":
    main()