def concat_elements_v1(slist, startpos, stoppos):
    if startpos < 0:
        start = 0
    else:
        start = startpos

    if stoppos > len(slist):
        stop = len(slist)
    else:
        stop = stoppos

    if stoppos < startpos:
        return ''

    for i in range(start, stop+1):
        if i == start:
            result = slist[i]
        else:
            result += slist[i]

    return result