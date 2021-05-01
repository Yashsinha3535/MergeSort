def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        #Recursive call on each
        mergeSort(left)
        mergeSort(right)

        #Iterators for both halves
        i = 0 #Left
        j = 0 #Right

        #Iterator for the array
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i+= 1
            else:
                array[k] = right[j]
                j += 1
            #move to next slot
            k += 1
        
        #for remaining slots
        while i < len(left):
            array[k] = left[i]
            i += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1


Array = [22,2,3,45,55,66,100,200]
mergeSort(Array)
print(Array)