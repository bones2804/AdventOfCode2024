def is_list_safe(numbers):
    #return a boolean list of whether each number is safe
    return [is_safe(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)]

def is_safe(number1, number2):
    diff = number1 - number2
    return diff == 0 or abs(diff) < 4

def is_list_ascending_or_descending(numbers):
    return all(is_ascending(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)) or all(is_descending(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1))   

def is_ascending(number1, number2):
    return number1 < number2

def is_descending(number1, number2):
    return number1 > number2

def main():
    # Read the input file
    lines = open('inputs.txt').readlines()

    safe_count = 0;
    
    # Process each line from the input
    for line in lines:
        # Remove trailing whitespace and newlines
        line = line.strip()

        #slpit line by spaces
        numbers = line.split(' ')

        #convert to int
        numbers = [int(num) for num in numbers]
        if(all(is_list_safe(numbers)) and is_list_ascending_or_descending(numbers)):
            safe_count += 1


    print(safe_count)


if __name__ == "__main__":
    main()
