def selectionSort(dizgi):
    for i in range(len(dizgi)):
        selectedIndex = i
        for j in range(i+1,len(dizgi)):
            if dizgi[selectedIndex] > dizgi[j]:
                selectedIndex = j
        dizgi[i], dizgi[selectedIndex] = dizgi[selectedIndex], dizgi[i]
    
dizi = [5,4,9,10,2,8]
selectionSort(dizi)