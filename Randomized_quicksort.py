import random

def randomized_quicksort(A):
    """
    Sorts an array in place using the randomized Quicksort algorithm.
    """
    def _quicksort(elements, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = randomized_partition(elements, low, high)
            # Recursively sort elements before and after partition
            _quicksort(elements, low, pivot_index - 1)
            _quicksort(elements, pivot_index + 1, high)

    def randomized_partition(elements, low, high):
         
        #Randomly selects a pivot and partitions the array around it.
         
        # Select a random pivot index between low and high
        pivot_index = random.randint(low, high)
        # Swap the pivot with the last element
        elements[pivot_index], elements[high] = elements[high], elements[pivot_index]
        return partition(elements, low, high)

    def partition(elements, low, high):
        """
        Partitions the array around the pivot element.
        """
        pivot = elements[high]  # Pivot is now randomly selected
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
    sample_array = [13, 7, 16, 9, 1, 5]
    print("Original array:", sample_array)
    randomized_quicksort(sample_array)
    print("Sorted array:", sample_array)
