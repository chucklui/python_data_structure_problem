from re import search


def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    nums_freq = {}
    for num in lst:
        nums_freq[num] = (nums_freq.get(num) or 0) + 1 

    return nums_freq.get(search_term,0)
