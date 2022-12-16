"""
Something here
"""
def linear_search(array,value):
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
