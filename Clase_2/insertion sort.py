#Mendoza Hilasaca Emerson Danny
#20190631
#Ejercicio 1

def insertion(array):    
    j = 0
    while j < len(array):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1  
        array[i + 1] = key
        j += 1  
    return array

numbers = [10, 4, 5, 8, 7, 2]

print(insertion(numbers))

