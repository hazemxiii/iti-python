unoredered_numbers = [13,6,28,3,20,12,9,10,5,8]

def bubble_sort(numbers):
    for i in range(0,len(numbers)-1):
        swapped = False
        for j in range(0,len(numbers)-i-1):
            compare_j = j+1
            if numbers[compare_j]<numbers[j]:
                temp = numbers[compare_j]
                numbers[compare_j]=numbers[j]
                numbers[j]=temp
                swapped=True
        if not swapped:
            return

bubble_sort(unoredered_numbers)
print(unoredered_numbers)