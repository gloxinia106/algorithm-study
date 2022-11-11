import sys

str = list(sys.stdin.readline().rstrip())
num = int(sys.stdin.readline().rstrip())
str_list = []

for _ in range(num):
    command = sys.stdin.readline().rstrip().split()

    if(command[0] == "L"):
        if(len(str) > 0):
            str_list.append(str.pop())
    
    elif(command[0] == "D"):
        if(len(str_list) > 0):
            str.append(str_list.pop())

    elif(command[0] == "B"):
        if(len(str) > 0):
            str.pop()
    
    else:
        str.append(command[1])

str_list.reverse()  
answer = str + str_list
print("".join(answer))