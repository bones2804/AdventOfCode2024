import re
def find_at_position(data, position):
    if position[0] >= 0 and position[0] < len(data) and position[1] >= 0 and position[1] < len(data[position[0]]):
        #check if th value is a number
        if re.match(r"^\d+$", data[position[0]][position[1]]):
            return int(data[position[0]][position[1]])
    return None

def find_path(data, position, blank):
    value = find_at_position(data, position)
    blank[position[0]][position[1]] = value
    if value == 9:
        return 1
    else:
        sum = 0
        #get the positions of the 4 directions
        directions = [(position[0]-1, position[1]), (position[0]+1, position[1]), (position[0], position[1]-1), (position[0], position[1]+1)]
        for direction in directions:
            if find_at_position(data, direction) is not None:
                if find_at_position(data, direction) == value + 1:
                    sum += find_path(data, direction, blank)

        #print(value, sum)
        #print_blank(blank)
        #print()
        return sum
    
def print_blank(blank):
    for row in blank:
        print(row)

def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    total_sum = 0

    #blank copy of data all negative 1s 
    blank = [[-1 for _ in range(len(data[0]))] for _ in range(len(data))]
    

    for i in range(len(data)):
        for j in range(len(data[i])):
            position = (i, j)
            value = find_at_position(data, position)
            #if avlue is 0, find the path and print the number of 9s in the path
            if value == 0:
                for k in range(len(blank)):
                    for l in range(len(blank[i])):
                        blank[k][l] = -1
                paths = find_path(data, position, blank)
                #print_blank(blank)
                print(paths)
                total_sum += paths

    print(total_sum)

if __name__ == "__main__":
    main()