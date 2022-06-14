def bubble_sort(seq):
    """
    This function sorts lists of integers:

    >>> bubble_sort([3, 2, 1])
    [1, 2, 3]

    as well as characters:

    >>> bubble_sort(['h', 'e', 'l', 'l', 'o'])
    ['e', 'h', 'l', 'l', 'o']
    """
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] == seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                changed = True
    return seq
