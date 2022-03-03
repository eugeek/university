def bubbleSort(m):
    size = len(m)
    for i in range(size):
        for j in range(size - 1):
            if m[j] > m[j+1]:
                t = m[j+1]
                m[j+1] = m[j]
                m[j] = t
    return m

def reverseBubbleSort(m):
    size = len(m)
    for i in range(size - 1, 0, -1):
        for j in range(size - 2, -1, -1):
            if m[j] > m[j+1]:
                t = m[j+1]
                m[j+1] = m[j]
                m[j] = t
    return m


def selectionSort(m):
    size = len(m)
    for i in range(size - 1):
        minI = i
        for j in range(i+1, size):
            if m[j] < m[minI]:
                minI = j
        t = m[i]
        m[i] = m[minI]
        m[minI] = t
        
    return m

def insertionSort(m):
    size = len(m)
    for i in range(size):
        t = m[i]
        j = i - 1
        while j >= 0 and t < m[j]:
            m[j+1] = m[j]
            j -= 1
        m[j+1] = t
    return m

arr = [4,12,7,4,1,6,10,-4,-10]
print('Array was: ', arr)
print(bubbleSort(arr))
print(reverseBubbleSort(arr))
print(selectionSort(arr))
print(insertionSort(arr))
