def concat_elements_v2(slist, startpos, stoppos):
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

    slice = slist[start:stop+1]
    result = ''.join(slice)
    return result