def main():
    with open('input.txt', 'r') as file:
        line = file.read()

    sum = 0

    #for line in lines:
    sub_string = line

    while 'mul(' in sub_string:
        mulindex = sub_string.find('mul(')
        dontindex = sub_string.find("don't()")
        if dontindex != -1 and dontindex < mulindex:
            sub_string = sub_string[sub_string.find('do()') + 4:]   
            continue                       
        sub_string = sub_string[sub_string.find('mul('):]
        if ')' in sub_string:
            mul_string = sub_string[:sub_string.find(')') + 1]
            if ' ' in mul_string:
                sub_string = sub_string[1:]
                continue
            numbers_string = mul_string[mul_string.find('(') + 1:mul_string.find(')')].split(',')
            if len(numbers_string) != 2:
                sub_string = sub_string[1:]
                continue
            #ensure that the numbers are integers if they are not continue the loop
            try:
                numbers = [int(num) for num in numbers_string]
            except ValueError:
                sub_string = sub_string[sub_string.find('mul(') + 4:]
                continue

            sub_string = sub_string[sub_string.find(')') + 1:]
            sum += numbers[0] * numbers[1]

    print(sum)
            

if __name__ == "__main__":
    main()
