def linear_search(array,value):
   pass
  
 
  
def merge_sort(lst):
    pass

  
  
def binary_search(list_of_values, value):
    pass
  
  
  
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
   pass
