import re

def main():
    with open("input.txt", 'r') as file:
        lines = file.read().splitlines()

    #create a list of strings for the vertical lines
    vertical_lines = [""] * len(lines[0])
    diagonal_lines_1 = [""] * (len(lines)*2 -1)
    diagonal_lines_2 = [""] * (len(lines)*2 -1)
    for line in lines:
        for i, char in enumerate(line):
            vertical_lines[i] += char

    for i in range(len(lines)):
        for j in range(i + 1):
            diagonal_lines_1[i] += lines[i - j][j]
            diagonal_lines_2[i] += lines[len(lines) - 1 - i + j][j]
            if(i != len(lines) - 1):
                diagonal_lines_1[len(diagonal_lines_1) -1 - i] += lines[len(lines[0]) - 1 - j][len(lines) - 1 - i + j]
                diagonal_lines_2[len(diagonal_lines_2) -1 - i] += lines[j][len(lines) - 1 - i + j]

    sum = 0
    pattern = r'(XMAS)'

    horizontal_sum = 0
    for i in range(len(lines)):
        matches = re.findall(pattern, lines[i])
        #print(str(len(matches)) + " matches for horizontal line " + str(i))
        #print(lines[i])
        horizontal_sum += len(matches)
        #check the reverse
        matches = re.findall(pattern, lines[i][::-1])
        horizontal_sum += len(matches)
    print(horizontal_sum)

    vertical_sum = 0
    for i in range(len(vertical_lines)):
        matches = re.findall(pattern, vertical_lines[i])
        #print(str(len(matches)) + " matches for vertical line " + str(i))
        #print(vertical_lines[i])
        vertical_sum += len(matches)
        #check the reverse
        matches = re.findall(pattern, vertical_lines[i][::-1])
        vertical_sum += len(matches)
    print(vertical_sum)

    diagonal_sum_1 = 0
    for i in range(len(diagonal_lines_1)):
        matches = re.findall(pattern, diagonal_lines_1[i])
        #print(str(len(matches)) + " matches for diagonal line 1 " + str(i))
        #print(diagonal_lines_1[i])
        diagonal_sum_1 += len(matches)
        #check the reverse
        matches = re.findall(pattern, diagonal_lines_1[i][::-1])
        diagonal_sum_1 += len(matches)
    print(diagonal_sum_1)

    diagonal_sum_2 = 0
    for i in range(len(diagonal_lines_2)):
        matches = re.findall(pattern, diagonal_lines_2[i])
        #print(str(len(matches)) + " matches for diagonal line 2 " + str(i))
        #print(diagonal_lines_2[i])
        diagonal_sum_2 += len(matches)
        #check the reverse
        matches = re.findall(pattern, diagonal_lines_2[i][::-1])
        diagonal_sum_2 += len(matches)
    print(diagonal_sum_2)

    print(horizontal_sum + vertical_sum + diagonal_sum_1 + diagonal_sum_2)

if __name__ == "__main__":
    main()