def sort_a_list(array: list[int]) -> None:
    length = len(array)
    for i in range(length):
        for j in range(i, length):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

