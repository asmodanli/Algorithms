def mergeSort(arr):
    mid = len(arr)//2
    if len(arr) > 1:
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
    
    i, j, k = 0, 0, 0

 #   while i < len

dizi = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
mergeSort(dizi)