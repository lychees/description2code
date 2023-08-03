import sys
testCase = int(raw_input())

def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

while (testCase>0):
    try:
        line = raw_input()
    except KeyboardInterrupt:
        break

    if not line:
        break
    else:
        temp = line.split(" ")
        orig1 = temp[0]
        orig2 = temp[1]
        temp[0]=temp[0].replace("#","")
        temp[1] = temp[1].replace("#","")
        if temp[0]==temp[1]:
            listA1 = findOccurences(orig1, "A")
            listA2 = findOccurences(orig2, "A")
            listB = findOccurences(orig1, "B")
            listB2 = findOccurences(orig2, "B")
            flag =1
            for index in range(len(listA1)):
                if listA1[index]<listA2[index]:
                    flag=0
            for index in range(len(listB)):
                if listB2[index]<listB[index]:
                    flag =0
            if flag ==0:
                print "No"
            else:
                print "Yes"
        else:
            print "No"
    testCase-=1

