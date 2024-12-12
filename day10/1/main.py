import re
def find_at_position(data, position):
    if position[0] >= 0 and position[0] < len(data) and position[1] >= 0 and position[1] < len(data[position[0]]):
        return data[position[0]][position[1]]
    return None

def find_path(data, position):
    value = find_at_position(data, position)
    #check above, below, left, right if thier value is exactly 1 more than the current value
    #perform a depth first search until you find all 9s
    #return the number of unique 9s found
    visited = set()
    stack = [(position, value)]
    visited.add(position)
    
    while stack:
        current_pos, current_val = stack.pop()
        
        # Check all 4 directions
        directions = [
            (current_pos[0]-1, current_pos[1]), # up
            (current_pos[0]+1, current_pos[1]), # down
            (current_pos[0], current_pos[1]-1), # left
            (current_pos[0], current_pos[1]+1)  # right
        ]
        
        for next_pos in directions:
            if next_pos not in visited:
                next_val = find_at_position(data, next_pos)
                if next_val is not None:
                    next_val = int(next_val)
                    current_val = int(current_val)
                    if next_val == (current_val + 1):
                        stack.append((next_pos, next_val))
                        visited.add(next_pos)
    
    # Count number of 9s in visited positions
    nine_count = sum(1 for pos in visited if int(find_at_position(data, pos)) == 9)
    return nine_count

def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    total_sum = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            position = (i, j)
            value = find_at_position(data, position)
            #if avlue is 0, find the path and print the number of 9s in the path
            if value == '0':
                total_sum += find_path(data, position)

    print(total_sum)

if __name__ == "__main__":
    main()