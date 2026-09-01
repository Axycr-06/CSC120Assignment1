Expected Behavior
Write a function concat_elements_v2(slist, startpos, stoppos), where slist is a list of strings and startpos and stoppos are integers, that concatenates the elements of slist starting at position startpos and ending at position stoppos (inclusive) and returns the resulting string.

Your code should behave reasonably for all values of startpos and stoppos: if startpos is negative, concatenation should start with the first element of slist; if stoppos ≥ len(slist), concatenation should stop at the last element of slist. If startpos > stoppos it should return the empty string. See the examples below.

Programming Requirements
Solve this problem without explicitly iterating over the list. One way to do this involves a combination of slicing and join().
Examples

    concat_elements_v2(['aa','bb','cc','dd'], 1, 3)
    return value: 'bbccdd'

    concat_elements_v2(['aa','bb','cc','dd'], -1, 1)
    return value: 'aabb'

    concat_elements_v2(['aa','bb','cc','dd'], -9, 9)
    return value: 'aabbccdd'

    concat_elements_v2(['aa','bb','cc','dd'], 3, 3)
    return value: 'dd'

    concat_elements_v2(['aa','bb','cc','dd'], 3, 1)
    return value: ''