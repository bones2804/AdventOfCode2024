import re
distinct_positions = {}

def main():
    global distinct_positions
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
        
    take_step(data, position, state)

    print(len(distinct_positions))


def take_step(data, position, state):
    global distinct_positions
    current_position = position
    current_state = state

    while True:
        if not distinct_positions.get(current_position):
            distinct_positions[current_position] = True

        # Calculate new position based on current state
        match current_state:
            case 0:
                new_position = (current_position[0] - 1, current_position[1])
            case 1:
                new_position = (current_position[0], current_position[1] + 1)
            case 2:
                new_position = (current_position[0] + 1, current_position[1])
            case 3:
                new_position = (current_position[0], current_position[1] - 1)

        target = get_position(data, new_position[0], new_position[1])

        match target:
            case "#":
                current_state = rotate_direction(current_state)
            case None:
                return
            case _:
                current_position = new_position

def rotate_direction(state):
    return (state + 1) % 4

def get_position(data, i, j):
    if i >= 0 and i < len(data) and j >= 0 and j < len(data[i]):
        return data[i][j]
    return None

if __name__ == "__main__":
    main()