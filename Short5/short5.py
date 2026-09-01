def grid_is_square(arglist):
    for row in arglist:
        if len(row) != len(arglist):
            return False
    return True