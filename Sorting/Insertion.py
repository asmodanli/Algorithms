def insertionSort(arr):
    for i in range(1, len(arr)):
        selected = arr[i]
        j = i -1
        while j >= 0:
            if selected < arr[j]:
                arr[j+1] = arr[j]
                arr[j] = selected
                j -=1
            else:
                break

dizi = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
insertionSort(dizi)