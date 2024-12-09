graph = {}

def main():
    with open('input.txt', 'r') as file:
        content = file.read()
        sections = content.split('\n\n')
        
        #find max number
        input_lines = sections[1].split('\n')
        numbers = []
        for line in input_lines:
            numbers.extend(line.split(','))

        #create graph
        create_graph((int)(max(numbers)))


        #add edges
        rule_lines = sections[0].split('\n')
        for line in rule_lines:
            split_line = line.split('|')
            add_edge(split_line[1], split_line[0])

        incorrect_numbers = []
        for line in sections[1].split('\n'):
            numbers = line.split(',')
            if not check_rule(numbers):
                incorrect_numbers.append(numbers)

        #print(incorrect_numbers)
        total = 0
        for numbers in incorrect_numbers:
            #print(numbers)
            numbers = graph_sort(numbers)
            #print("sorted: ", numbers)
            middle_number = int(numbers[len(numbers) // 2])
            #print(middle_number)
            total += middle_number

        print(total)

        


        
        
def create_graph(max_number):
    global graph

    print(max_number)

    graph = {}
    for i in range(max_number + 1):
        graph[i] = []
    return graph

def add_edge(u, v):
    global graph
    graph[int(u)].append(int(v))

def check_rule(numbers):
    global graph
    numbers = [int(n) for n in numbers]
    for i in range(len(numbers) - 1):
        if numbers[i] not in graph:
            continue
        for j in range(i + 1, len(numbers)):
            if numbers[j] in graph[numbers[i]]:
                return False
    return True

def graph_sort(numbers):
    global graph
    numbers = [int(n) for n in numbers]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] in graph[numbers[i]]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


if __name__ == "__main__":
    main()