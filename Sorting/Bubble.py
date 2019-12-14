def bubbleSort(dizgi):
    for i in range(len(dizgi)):
        for j in range(i+1, len(dizgi)):
            if dizgi[i] > dizgi[j]:
                dizgi[i], dizgi[j] = dizgi[j], dizgi[i]


dizi = [50,9,10,2,7,99,36,8,45]
bubble(dizi)