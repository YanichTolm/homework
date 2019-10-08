def SelectionSort(array):
    a = array
    for i in range(len(a)):
        idxMin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idxMin]:
                idxMin = j
        tmp = a[idxMin]
        a[idxMin] = a[i]
        a[i] = tmp
    return a


print ("The Selection sort:")
arrSelect = [152, 679, 866, 683, 443, 613, 495, 195, 433, 403, 134, 645, 340, 303, 839]
print(SelectionSort(arrSelect))


def InsertionSort(array):
    a = array
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j - 1] > v) and (j > 0):
            a[j] = a[j - 1]
            j = j - 1
        a[j] = v
        print(a)
    return a


print ("The Insertion sort:")
arrInsert = [589, 325, 103, 775, 136, 491, 569, 147, 442, 878, 257, 272, 658, 530, 838]
print(InsertionSort(arrInsert))


def BubbleSort(array):
    a = array
    i = 0
    while (i < len(a)):
     j = 0
     while (j < len(a) - i - 1):
        if (a[j] > a[j + 1]):
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
        j += 1
     i += 1
    return a


print ("The Bubble sort:")
arrBubble = [550, 346, 387, 452, 721, 833, 859, 561, 955, 38, 366, 764, 431, 694, 14]
print(BubbleSort(arrBubble))
