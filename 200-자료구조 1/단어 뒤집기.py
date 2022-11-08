num = int(input())

for _ in range(num):
    str_list = input().split()

    for str in str_list:
        i = -1
        for _ in range(len(str)):
            print(str[i], end="")
            i -= 1
        print(" ",end="")
    print()
