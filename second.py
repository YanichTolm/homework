from random import randrange
import time

from datetime import datetime

file = open("ai182.txt", "r")
alist = []
checkfirst = False
checksecond = False

while True:
    check = file.read(1)
    if not check:
        break

    if check == "1":
        check = file.read(1)
        if check == '6':
            checkfirst = True
            check = file.read(1)
            if check == ":":
                checksecond = True

    if checkfirst == True and checksecond == True:
        file.seek(file.tell() + 1)
        check = file.read(1)
        while check != "}":
            alist.append(int(check))
            check = file.read(1)
        break


def mergesort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        toleft = alist[:mid]
        toright = alist[mid:]
        mergesort(toleft)
        mergesort(toright)
        i = 0
        j = 0
        k = 0
        while i < len(toleft) and j < len(toright):
            if toleft[i] < toright[j]:
                alist[k] = toleft[i]
                i = i + 1
            else:
                alist[k] = toright[j]
                j = j + 1
            k = k + 1
        while i < len(toleft):
            alist[k] = toleft[i]
            i = i + 1
            k = k + 1
        while j < len(toright):
            alist[k] = toright[j]
            j = j + 1
            k = k + 1


def heap(alist, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and alist[largest] < alist[l]:
        largest = l
    if r < n and alist[largest] < alist[r]:
        largest = r
    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        heap(alist, n, largest)


def heapsort(alist):
    n = len(alist)

    for i in range(n, -1, -1):
        heap(alist, n, i)

    for i in range(n - 1, 0, -1):
        alist[i], alist[0] = alist[0], alist[i]
        heap(alist, i, 0)


def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        p = x[0]
        i = 0
        for j in range(len(x) - 1):
            if x[j + 1] < p:
                x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
                i += 1
        x[0], x[i] = x[i], x[0]
        tofirst = quicksort(x[:i])
        tosecond = quicksort(x[i + 1:])
        tofirst.append(x[i])
        return tofirst + tosecond


file.close()

# duration of the merge sort: 0:00:00.000998
start_time = datetime.now()
mergesort(alist)
print(alist)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# duration of the heap sort: 0:00:00.000995
start_time = datetime.now()
heapsort(alist)
print(alist)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# duretion of the quick sort: 0:00:00.000997
start_time = datetime.now()
quicksort(alist)
print(alist)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

# in conclusion: all sorts are time-efficient
# difference is not significant, but heap sort takes a little less time
# thank you for attention ^^
