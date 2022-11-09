num = int(input())

stack = []
stack_num = 0
pri_str = ""

for _ in range(num):
    seq_num = int(input())
    while(stack_num < seq_num):
        pri_str += "+"
        stack_num +=1
        stack.append(stack_num)

    if(stack[-1] == seq_num):
        stack.pop()
        pri_str +="-"
    else:
        pri_str = "NO"
        break

if(pri_str == "NO"):
    print(pri_str)
else:
    print('\n'.join(pri_str))