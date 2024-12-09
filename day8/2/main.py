char_dict = {}
antinodes = {}  # Initialize as dictionary here

def calculate_antinodes(position1, position2, data):
    distance = (position1[0] - position2[0], position1[1] - position2[1])
    antinodes = []
    antinodes.append(position1)
    antinodes.append(position2)
    current_position = position1
    while current_position is not None:
        current_position = (current_position[0] + distance[0], current_position[1] + distance[1])
        if current_position[0] >= 0 and current_position[0] < len(data) and current_position[1] >= 0 and current_position[1] < len(data[current_position[0]]):
            antinodes.append(current_position)
        else:
            current_position = None
    current_position = position2
    while current_position is not None:
        current_position = (current_position[0] - distance[0], current_position[1] - distance[1])
        if current_position[0] >= 0 and current_position[0] < len(data) and current_position[1] >= 0 and current_position[1] < len(data[current_position[0]]):
            antinodes.append(current_position)
        else:
            current_position = None

    return antinodes

def main():
    global char_dict
    global antinodes
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != ".":
                if data[i][j] in char_dict:
                    char_dict[data[i][j]].append((i, j))
                else:
                    char_dict[data[i][j]] = [(i, j)]

    for char in char_dict:
        for i in range(len(char_dict[char])):
            for j in range(i + 1, len(char_dict[char])):
                antinode_pair = calculate_antinodes(char_dict[char][i], char_dict[char][j], data)
                for antinode in antinode_pair:
                    if antinode is not None:
                        antinodes[antinode] = True

    data_copy = [list(line) for line in data]  # Convert each line to a list of characters
    for antinode in antinodes:
        data_copy[antinode[0]][antinode[1]] = "#"
    data_copy = [''.join(line) for line in data_copy]  # Convert each list of characters back to a string
    for line in data_copy:
        print(line)
    print(len(antinodes))

if __name__ == "__main__":
    main()
