class Node:
    def __init__(self, value, opperation):
        self.value = value
        self.opperation = opperation
        self.children = []

    def add_value(self, value):
        if(len(self.children) == 0):
            self.children.append(Node(value, '+'))
            self.children.append(Node(value, '*'))
        else:
            for child in self.children:
                child.add_value(value)

    def calc_value(self, sum):
        if(self.opperation == '*'):
            return sum * self.value
        else:
            return sum + self.value
        
    def find_answer(self, number, sum):
        sum = self.calc_value(sum)
        if(len(self.children) == 0):
            if(sum == number):
                return True
            else:
                return False
        else:
            return self.children[0].find_answer(number, sum) or self.children[1].find_answer(number, sum)

class Tree:
    def __init__(self, value):
        self.root = Node(value, None)
    
    def add_value(self, value):
        self.root.add_value(value)

    def find_answer(self, number):
        return self.root.find_answer(number, 0)

def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()

    sum = 0

    for line in data:
        #get everything before the colon
        answer = line.split(":")[0].strip()
        #get everything after the colon
        paramters = line.split(":")[1].strip().split(" ")
        #create a tree with the root value being the first number
        tree = Tree(int(paramters[0]))
        #add the rest of the numbers to the tree
        for i in range(1, len(paramters)):
            tree.add_value(int(paramters[i]))
        #find the answer
        if(tree.find_answer(int(answer))):
            sum += int(answer)

    print(sum)

if __name__ == "__main__":
    main()

