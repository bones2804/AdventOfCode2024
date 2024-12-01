def main():
    # Read input from file
    try:
        with open('input.txt', 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        print("Error: input.txt file not found")
        return
    
    print("start")

    #create 2 lists to store the numbers
    list1 = []
    list2 = []

    # Process data here
    for line in data:
        print(line)
        line = line.strip()  # Remove trailing whitespace and newline
        
        # Split the line into two numbers
        numbers = line.split()
        if(len(numbers) >= 2):
            number1 = int(numbers[0])
            number2 = int(numbers[1])

            list1.append(number1)
            list2.append(number2)

    #sort the lists
    list1.sort()
    list2.sort()

    #varible to store the sum of the differences
    sum_of_differences = 0

    for i in range(len(list1)):
        sum_of_differences += abs(list1[i] - list2[i])

    print(sum_of_differences)




if __name__ == "__main__":
    main() 