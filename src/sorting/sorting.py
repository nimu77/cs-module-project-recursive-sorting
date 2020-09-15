# TO-DO: complete the helper function below to merge 2 sorted arrays
# two arrays that are each already sorted
# this function returns a single sorted array of all the elements from
# arrA and arrB
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # pre-allocating our output array with the number of elements
    # we know it will hold at the end
    merged_arr = [0] * elements

    # Your code here
    start_a = 0
    start_b = 0
    # init pointers to the beginning of arrA and arrB
    # compare the elements those pointers are pointing at
    # whichever element is less than or equal
    # loop so long as both
    #  pointers are in range of their
    # respective arrays

    output = []
    for i in range(0, len(merged_arr)):
        if arrA[start_a] > arrB[start_b]:
            output.append(arrB[start_b])
            start_b += 1
        elif arrA[start_a] < arrB[start_b]:
            output.append(arrA[start_a])
            start_a += 1

    return output

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here




    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here

