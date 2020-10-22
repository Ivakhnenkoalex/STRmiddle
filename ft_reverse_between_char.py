def ft_len(str):
    a = 0
    for i in str:
        a += 1
    return (a)

def ft_reverse_between_char(char,str):
    d = ft_len(str)
    z = d
    i = 0
    k = 0
    o = ''
    while d > i:
        if str[i] == char:
            k = k + 1
        i = i + 1
    if k == 1:
        return -1
    if k == 0:
        return -2
    if k >= 2:
        k2 = k
        d = z
        i = 0
        while d > i:
            if str[i] == char:
                k1 = i
                break
            i = i + 1
        i = 0
        d = z
        while d > i:
            if str[i] == char:
                k2 = i
            i = i + 1
        o += str[0::k1]
        o += str[k2::z-1]
        return o
print(ft_reverse_between_char("d",'jdkhhdg'))




