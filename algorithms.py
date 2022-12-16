def linear_search(list_of_values, value):
    """
    (list, int) -> int
    Function finds first index of value. If value is not in array, function will return -1
    >>> linear_search([1,2,3,414,1424,1241,24,124,124,1,412,4,],1)
    0
    """
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1
  

def merge(lst1,lst2):
    """
    help function for merge_sort
    """
    res = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    while i < len(lst1):
        res.append(lst1[i])
        i += 1
    while j < len(lst2):
        res.append(lst2[j])
        j += 1
    return res
  
def merge_sort(lst):
    """
    lst -> lst
    returns a sorted list
    >>> merge_sort([5,7,2,1,9,7,4,8,3])
    [1, 2, 3, 4, 5, 7, 7, 8, 9]
    """
    if len(lst) == 1:
        return lst
    lst1 = merge_sort(lst[0:(len(lst)//2)])
    lst2 = merge_sort(lst[(len(lst)//2)::])
    return merge(lst1,lst2)


  
  
def binary_search(list_of_values, value):
    """
    Executes binary search
    >>> binary_search([1, 3, 15, 23, 32, 57, 99, 200, 777], 99)
    6
    """
    start = 0
    end = len(list_of_values) - 1
    partition = 0
 
    while start <= end:
        partition = (start + end) // 2
        if list_of_values[partition] < value:
            start = partition + 1
        elif list_of_values[partition] > value:
            end = partition - 1
        else:
            return partition
    return -1

  
  
 
def selection_sort(lst):
    '''
    Sorts a list with an algoritm of selection.
    >>> selection_sort([2, 4, 3, 1])
    [1, 2, 3, 4]
    >>> selection_sort([10000000, 6567, 0, 4567, 78])
    [0, 78, 4567, 6567, 10000000]
    '''
    for i in range(len(lst)):
        min_i = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_i]:
                min_i = j
        lst[min_i], lst[i] = lst[i], lst[min_i]
    return lst
  
  
  
def quick_sort(lst):
    """
    The function takes a list and sorts it using a method quick sort
    >>> quick_sort([ 23, 67, 2, 4, 7, 89])
    [2, 4, 7, 23, 67, 89]
    """
    start = 0
    end_lis = len(lst) - 1
    poil = lst[end_lis]
    while start <= end_lis:
        while lst[start] < poil:
            start = start + 1
        while poil < lst[end_lis]:
            end_lis = end_lis - 1
        if start <= end_lis:
            lst[start], lst[end_lis] = lst[end_lis], lst [start]
            start = start + 1
            end_lis = end_lis - 1
    if 0 < end_lis:
        lst[0:end_lis + 1] = quick_sort(lst[0:end_lis + 1])
    if start < len(lst):
        lst[start: len(lst)] = quick_sort(lst[start: len(lst)])
    return lst

