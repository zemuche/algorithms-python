def binsearchrecur(sequence, item, start=0, stop=None):
    if len(sequence) == 0:
        return False
    if stop is None:
        stop = len(sequence) - 1
    if start == stop and item == sequence[start]:
            return start
    if sequence[start] > item or sequence[stop] < item:
        return False
    mid = (stop + start) // 2
    if item == sequence[mid]:
        return mid
    elif item < sequence[mid]:
        return binsearchrecur(sequence, item, start, mid - 1)
    else:
        return binsearchrecur(sequence, item, mid + 1, stop)


def binsearchiter(sequence, item, start=0, stop=None, return_index=True):
    if len(sequence) == 0:
        return False
    found = False
    if stop is None:
        stop = len(sequence) - 1
    while not found and start < stop:
        mid = (start + stop) // 2
        if item == sequence[mid]:
            found = True
            if return_index is True:
                return mid
        elif item > sequence[mid]:
            start = mid + 1
        else:
            stop = mid
    return found


def linsearch(sequence, target, start=0, end=None):
    """Search linearly for target in sequence between
    start and end, inclusive."""
    if end is None:
        end = len(sequence) - 1
    for i, value in enumerate(sequence[start:end+1], start):
        if value == target:
            return i
    else:
        return False


def main():
    alist = [43, 5, 0, 3, 86, 45, -8, 12]
    print(alist)
    a = linsearch(alist, 3)
    alist.sort()
    print(alist)
    b = binsearchrecur(alist, 98)
    print(a, b)


if __name__ == '__main__':
    main()
