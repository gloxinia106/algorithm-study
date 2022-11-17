string = input()

answer = 0
stack = []

for index in range(len(string)):
    if(string[index] == "("):
        stack.append(string[index])
    elif(string[index] == ")"):
        if(string[index-1] == "("):
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer +=1

print(answer)