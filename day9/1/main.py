class Block:
    def __init__(self, id, length):
        self.id = id
        self.length = length
        self.next = None
        self.prev = None

    def copy(self):
        return Block(self.id, self.length)

    def is_empty(self):
        return self.id is None
    
    def add_after(self, block):
        if self.next is not None:
            self.next.prev = block
            block.next = self.next
        block.prev = self
        self.next = block

    def remove_block(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev

class BlockList:
    def __init__(self):
        self.head = None

    def append(self, block):
        if self.head is None:
            self.head = block
        else:
            self.tail().add_after(block)

    def tail(self):
        current = self.head
        while current.next is not None:
            current = current.next
        return current


    def print(self):
        output = ""
        current = self.head
        while current is not None:
            if not current.is_empty():
                output += str(current.id) * current.length
            else:
                output += "." * current.length
            current = current.next
        return output
    
    def to_array(self):
        output = []
        current = self.head
        while current is not None:
            if not current.is_empty():
                temp = [current.id] * current.length
                output.extend(temp)
            else:
                output.extend([-1] * current.length)
            current = current.next
        return output

def decode_line(input_line):
    id = 0;
    output = BlockList()
    for i in range(len(input_line)):
        if i%2 == 0:
            #for j in range(int(input_line[i])):
            output.append(Block(id, int(input_line[i])))
            id += 1
        else:
            output.append(Block(None, int(input_line[i])))
    return output


def move_blocks(list):
    current = list.tail()
    while current is not None:
        if not current.is_empty():
            prev = list.head
            while prev is not None and prev != current:
                if prev.is_empty():
                    if prev.length == current.length:
                        #save our 2 blocks
                        current_copy = current.copy()
                        prev_copy = prev.copy()
                        temp_prev = current.prev
                        prev.prev.add_after(current_copy)
                        current.add_after(prev_copy)
                        current.remove_block()
                        prev.remove_block()
                        break
                    elif prev.length > current.length:
                        current_copy = current.copy()
                        prev_copy = prev.copy()
                        temp_prev = current.prev
                        prev.prev.add_after(current_copy)
                        prev.length -= current.length
                        current.add_after(Block(None,current.length))
                        current.remove_block()
                        current = temp_prev
                        break
                prev = prev.next
        current = current.prev
        if current is not None:
            print(current.id)
    return list

def calc_checksum(input_line):
    sum = 0
    for i in range(len(input_line)):
        if(input_line[i] != -1):
            sum += int(input_line[i]) * (i)
    return sum

def main():
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    
    for line in data:
        line = decode_line(line)
        print('decoded: ',line.print())
        line = move_blocks(line)
        print('moved: ',line.print())
        checksum = calc_checksum(line.to_array())
        print('checksum: ',checksum)   

if __name__ == "__main__":
    main()