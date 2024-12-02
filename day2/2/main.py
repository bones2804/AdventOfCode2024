def is_list_safe(numbers):
    #return a boolean list of whether each number is safe
    return [is_safe(numbers[i], numbers[i+1]) for i in range(len(numbers) - 1)]

def is_safe(number1, number2):
    diff = number1 - number2
    return diff == 0 or abs(diff) < 4

def is_list_ascending_or_descending(numbers):
    #return a list of numbers 1 if ascending, -1 if descending, 0 if neither
    return [1 if is_ascending(numbers[i], numbers[i+1]) else -1 if is_descending(numbers[i], numbers[i+1]) else 0 for i in range(len(numbers) - 1)]

def is_ascending(number1, number2):
    return number1 < number2

def is_descending(number1, number2):
    return number1 > number2

def is_list_consistent(asc_desc_list):
    #return true if all numbers in the list are the same
    return all(asc_desc_list[i] == asc_desc_list[0] for i in range(len(asc_desc_list)))

def main():
    # Read the input file
    lines = open('inputs.txt').readlines()

    safe_count = 0;
    
    # Process each line from the input
    for line in lines:
        # Remove trailing whitespace and newlines
        line = line.strip()

        #split line by spaces
        numbers = line.split(' ')

        #convert to int
        numbers = [int(num) for num in numbers]
        print(numbers)
        #if all numbers are safe and the list is all ascending or all descending, then it is safe
        if(all(is_list_safe(numbers)) and is_list_consistent(is_list_ascending_or_descending(numbers))):
            safe_count += 1
        else:
            #find one element to remove to make the list safe
            for i in range(len(numbers)):
                #print(numbers[:i] + numbers[i+1:])
                #print(is_list_safe(numbers[:i] + numbers[i+1:]))
                #print(is_list_consistent(is_list_ascending_or_descending(numbers[:i] + numbers[i+1:])))
                if(all(is_list_safe(numbers[:i] + numbers[i+1:])) and is_list_consistent(is_list_ascending_or_descending(numbers[:i] + numbers[i+1:]))):
                    safe_count += 1
                    break

        print("")

    print(safe_count)


if __name__ == "__main__":
    main()
