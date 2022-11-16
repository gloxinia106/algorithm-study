string = input()

answer = []
revers = []
toggle = False


for char in string:
    if(char == "<"):
        toggle = True
        revers.reverse()
        answer += revers
        revers = []
        answer.append(char)
        continue

    if(char == ">"):
        toggle = False
        answer.append(char)
        continue
        
    if(toggle and char != " "):
        answer.append(char)
    elif(not toggle and char != " "):
        revers.append(char)
    else:
        revers.reverse()
        revers.append(" ")
        answer += revers
        revers = []

if(revers != []):
    revers.reverse()
    answer += revers
    revers = []

print("".join(answer))