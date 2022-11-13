zo_list_num , zo_num = map(int,input().split())

zo_list = [i+1 for i in range(zo_list_num)]

index = 0
answer_list = []

while len(zo_list) > 0:
    index += zo_num -1

    while(index >= len(zo_list)):
        index -= len(zo_list)
    
    a = zo_list.pop(index)
    answer_list.append(str(a))

answer = ", ".join(answer_list)
print(f"<{answer}>")