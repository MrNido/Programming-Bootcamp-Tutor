"""
   This is a simple and intuitive sorting algorithm. It repeatedly walks through the 
   sequence to be sorted, comparing two elements at once. If the two elements are in
   the wrong order, then swapping them are in the wrong order. The work of visiting 
   the sequence is repeated until no more exchanges are needed, which implies, the 
   sequence has been sorted. 
"""


def sort_a_list(array: list[int]) -> None:
    length = len(array)
    # Get the length of the input array, that will help the iteration.
    for i in range(length):
        for j in range(i, length):
            # For every positions in the list, compare the elements in it with all of 
            # the other elements on the right of it. There's no need to compare it with
            # the elements on the left of it since the left elements are already sorted.
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                # If the two elements are in the wrong order, then swap them.
                

