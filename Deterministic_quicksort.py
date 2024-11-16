def quicksort(A):
    
    #Sorts an array in place using the Quicksort algorithm.
    
    def _quicksort(elements, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = partition(elements, low, high)
            # Recursively sort elements before and after partition
            _quicksort(elements, low, pivot_index - 1)
            _quicksort(elements, pivot_index + 1, high)

    def partition(elements, low, high):
        
        #Partitions the array around a pivot element.

        #Parameters:
        #elements (list): The list of elements to be partitioned.
        #low (int): The starting index of the subarray.
        # high (int): The ending index of the subarray.

        pivot = elements[high]  # Choose the last element as pivot
        i = low - 1  # Pointer for the greater element
        for j in range(low, high):
            if elements[j] <= pivot:
                i += 1
                elements[i], elements[j] = elements[j], elements[i]  # Swap
        # Place the pivot in the correct position
        elements[i + 1], elements[high] = elements[high], elements[i + 1]
        return i + 1

    _quicksort(A, 0, len(A) - 1)

# Example usage:
if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    print("Original array:", sample_array)
    quicksort(sample_array)
    print("Sorted array:", sample_array)
