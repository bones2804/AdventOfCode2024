def main():
    with open('input.txt', 'r') as file:
        line = file.read()

    sum = 0

    #for line in lines:
    sub_string = line[line.find('mul('):]

    while 'mul(' in sub_string:
        print(sub_string)
        sub_string = sub_string[sub_string.find('mul('):]
        if ')' in sub_string:
            mul_string = sub_string[:sub_string.find(')') + 1]
            if ' ' in mul_string:
                print('space error')
                sub_string = sub_string[1:]
                continue
            numbers_string = mul_string[mul_string.find('(') + 1:mul_string.find(')')].split(',')
            if len(numbers_string) != 2:
                print('length error')
                sub_string = sub_string[1:]
                continue
            #ensure that the numbers are integers if they are not continue the loop
            try:
                numbers = [int(num) for num in numbers_string]
            except ValueError:
                print('cast error')
                sub_string = sub_string[sub_string.find('mul(') + 4:]
                continue

            sub_string = sub_string[sub_string.find(')') + 1:]
            sum += numbers[0] * numbers[1]

            print(mul_string)
            print(numbers[0], '*', numbers[1], '=', numbers[0] * numbers[1])

    print(sum)
            

if __name__ == "__main__":
    main()
