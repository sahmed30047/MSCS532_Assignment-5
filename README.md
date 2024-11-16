**Deterministic Quicksort**

Requirements Python 3 installed on the machine.

_Running the Script_
Save the provided code in a file named Assignment 5_Deterministic Quicksort.py. Open terminal. Navigate to the directory where you saved Assignment 5_Deterministic Quicksort.py. Run the script by typing python Assignment 5_Deterministic Quicksort.py and press Enter.

_Output_
Original array: [10, 7, 8, 9, 1, 5] Sorted array: [1, 5, 7, 8, 9, 10]

_Findings_
The divide-and-conquer approach is used in the Quicksort algorithm to efficiently sort an array. It divides the array into two halves around a pivot element, with elements on the left being less than the pivot and elements on the right being larger. The algorithm recursively sorts the partitions, resulting in a sorted array. Quicksort is efficient on large datasets, with an average time complexity of O(n log n), but its worst-case complexity is O(n^2) when the pivot divides the list into uneven partitions. For simplicity, this implementation uses the last element as the pivot, which can be modified to optimize performance using various pivot selection strategies.





**Randomized Quicksort
**
Requirements Python 3

_Running the Script_ 
Save the script in a file named Assignment 5_Randomized Quicksort.py. Open the terminal. Navigate to the directory where the file is saved. Execute the script by typing python Assignment 5_Randomized Quicksort.py and pressing Enter.

_Output_
Original array: [13, 7, 16, 9, 1, 5] Sorted array: [1, 5, 7, 9, 13, 16]

_Findings_
Randomized Partitioning - A random pivot element divides the array more evenly. This improves performance over regular Quicksort, especially on partially or fully sorted arrays.

Like Quicksort, the randomized version sorts the array in-place, requiring only a small, constant amount of storage space.

Like standard Quicksort, the average time complexity is O(n log n), but randomization reduces the worst-case scenario.
