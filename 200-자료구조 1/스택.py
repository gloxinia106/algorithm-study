import sys
num = int(input())

list = []

for _ in range(num):
    command = sys.stdin.readline().rstrip().split()

    if(command[0] == "push"):
        list.append(int(command[1]))

    elif(command[0] == "pop"):
        if(list == []):
            print(-1)
        else: 
            list_pop = list.pop()
            print(list_pop)
    
    elif(command[0] == "size"):
        list_size = len(list)
        print(list_size)
    
    elif(command[0] == "empty"):
        if(list == []):
            print(1)
        else: 
            print(0)
    
    elif(command[0] == "top"):
        if(list == []):
            print(-1)
        else:
            print(list[-1])

