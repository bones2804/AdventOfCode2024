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

    #varible to store the sum of the differences
    sum = 0

    for number in list2:
        if number in list1:
            sum += number

    print(sum)




if __name__ == "__main__":
    main() 