t = raw_input("")
t = int(t)
count = 0
while count < t:
    n, k, m = raw_input("").split(" ")

    n = int(n)
    k = int(k)
    m = int(m)

    list1 = list()

    for i in range(n):
        str1 = raw_input("")
        list1.append(str1)

    # print list1

    list2 = list()

    for seq in list1:
        seq = seq[:m]
        list2.append(seq)

    dictionary = dict()

    x = 0
    for item in list1:
        dictionary[item] = list2[x]
        x += 1

    # print dictionary

    temp = list()
    for key, val in dictionary.items():
        temp.append((val, key))
    temp.sort()

    print temp[k-1][1]
    count += 1


