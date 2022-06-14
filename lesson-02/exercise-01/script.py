listsElements = [4, 2, -1002, 201, -13, 3, 312, 1001, -1001, -1]

def newMin(elements):
    minValue = listsElements[0]
    for element in range(len(listsElements)):
        if listsElements[element] < minValue:
            minValue = listsElements[element]
    return minValue


print(f"Il numero più piccolo della lista {listsElements} e': {newMin(listsElements)}")




def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) -1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                
list_random = [5, 2, 1, 8, 4]
bubble_sort(list_random)
print(list_random)



# Bubble Sort
# Confronta il primo elemento con il secondo, e poi spostalo nel caso