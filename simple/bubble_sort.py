l = [9,8,7,6,5,4,3,2,1,0]

for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            tmp = l[i]
            l[i] = l[j]
            l[j] = tmp
        print(l)
    print(l)