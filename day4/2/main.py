import re

def main():
    with open("input.txt", 'r') as file:
        lines = file.read().splitlines()

    x_count = 0

    #foreach line find each 'A'
    for i in range(len(lines)):
        if(i > 0 and i < len(lines)-1):
            matches = re.finditer('A', lines[i])
            for m in matches:
                if(m.start(0) > 0 and m.start(0) < (len(lines[i])-1)):
                    l = [False] * 4;
                    #print(i, m.start(0), len(lines[i])-2)
                    l[0] = lines[i -1][m.start(0) -1] == 'M' and lines[i +1][m.start(0) +1] == 'S'
                    l[1] = lines[i -1][m.start(0) +1] == 'M' and lines[i +1][m.start(0) -1] == 'S'
                    l[2] = lines[i +1][m.start(0) -1] == 'M' and lines[i -1][m.start(0) +1] == 'S'
                    l[3] = lines[i +1][m.start(0) +1] == 'M' and lines[i -1][m.start(0) -1] == 'S'                    


                    if(l[0] + l[1] + l[2] + l[3] >= 1 and l[0] + l[1] + l[2] + l[3] < 2):
                        print(i, ' ', m.start(0))
                        print(lines[i-1][m.start(0) -1],'.', lines[i-1][m.start(0) +1])
                        print('.', lines[i][m.start(0)], '.')
                        print(lines[i+1][m.start(0) -1],'.', lines[i+1][m.start(0) +1])
                        print('')

                    #check if 2 of the 4 above are true
                    if(l[0] + l[1] + l[2] + l[3] == 2):
                        x_count += 1
                        

    print(x_count)


    

if __name__ == "__main__":
    main()