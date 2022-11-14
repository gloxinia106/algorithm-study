import sys
from collections import deque

deck = deque()

num = int(input())

for _ in range(num):
    command = sys.stdin.readline().rstrip().split()

    if(command[0] == "push_front"):
        deck.appendleft(command[1])
    elif(command[0] == "push_back"):
        deck.append(command[1])
    
    elif(command[0] == "pop_front"):
        if(not deck):
            print(-1)
        else:
            num = deck.popleft()
            print(num)
    elif(command[0] == "pop_back"):
        if(not deck):
            print(-1)
        else:
            num = deck.pop()
            print(num)
    elif(command[0] == "size"):
        list_size = len(deck)
        print(list_size)
    elif(command[0] == "empty"):
        if(not deck):
            print(1)
        else: 
            print(0)
    elif(command[0] == "front"):
        if(not deck):
            print(-1)
        else:
            num = deck.popleft()
            deck.appendleft(num)
            print(num)
            
    else:
        if(not deck):
            print(-1)
        else:
            num = deck.pop()
            deck.append(num)
            print(num)