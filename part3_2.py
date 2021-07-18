def modify_list(l):
    a = []
    for i in l:
        if ((i % 2) == 0):
            b = int(i / 2)
            a.append(b)
    l[ : ] = a