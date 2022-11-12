import sys
que = []

num = int(input())

for _ in range(num):
    command = sys.stdin.readline().rstrip().split()

    if(command[0] == "push"):
        que.append(int(command[1]))
    elif(command[0] == "pop"):
        if(que == []):
            print(-1)
        else:
            num = que.pop(0)
            print(num)
    elif(command[0] == "size"):
        list_size = len(que)
        print(list_size)
    elif(command[0] == "empty"):
        if(que == []):
            print(1)
        else: 
            print(0)
    elif(command[0] == "front"):
        if(que == []):
            print(-1)
        else:
            print(que[0])
    else:
        if(que == []):
            print(-1)
        else:
            print(que[-1])
