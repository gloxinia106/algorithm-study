num = int(input())

for _ in range(num):
    str_list = input()
    stack = []
    try:
        for i in range(len(str_list)):
            if str_list[i] == "(":
                stack.append(str_list[i])
            else:
                stack.pop()
        if(stack == []):
            print("YES")
        else:
            print("NO")
    except IndexError:
        print("NO")
